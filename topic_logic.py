#######################################################################################
# Author: Jackson O'Donnell
#
# Purpose: Hold a function to determine the topic category of a curriculum on the fly
#######################################################################################


#######################################################################################
# Function: calcCat
#
# Purpose: Calculate the topic category of the curriculum
#
# Return: One of the following topic categories
#
#       Extensive: All level 1 and 2 topics covered by required courses, some units of
#               level 3 topics covered.
#       Inclusive: All level 1 and 2 topics covered by required courses
#       Basic-Plus: All level 1 topics covered by required courses. Some level 2 topics
#               covered by required courses, remaining level 2 units covered by
#               optional courses.
#       Basic: All level 1 topics covered by required courses. Some level 2 topics
#               covered by required courses.
#       Unsatisfactory: All level 1 topics covered by required courses. Not enough
#               level 2 topics covered by required courses to be Basic.
#       Substandard: Some level 1 topics are NOT covered by required courses.
#
# Parameters:
#       target: A dictionary containing the primary key of the curriculum, as well as
#             the percentage of level 2 & 3 topic coverage required for coverage
#       mycursor: The cursor to execute the queries for information
#######################################################################################
def calcCat(target, mycursor):
    topicSQL = """SELECT topic.subject, topic.units, topic.topic_id, topic.topic_name
                  FROM curriculum, topic, topic_curric
                  WHERE topic_curric.topic_id = topic.topic_id
                  AND topic_curric.curric_assoc = curriculum.curric_name
                  AND curriculum.curric_name = %s
                  AND topic_curric.lvl = %s
                  GROUP BY topic.topic_id, topic.topic_name"""
    reqSQL = """SELECT courses.subj_code, courses.cred_hrs, courses.course_name
                FROM curriculum, curric_reqs, courses
                WHERE curric_reqs.req_for = curriculum.curric_name
                AND curric_reqs.course_name = courses.course_name
                AND curriculum.curric_name = %s AND curriculum.person_id = %s
                GROUP BY courses.course_name"""
    opSQL = """SELECT courses.subj_code, courses.cred_hrs, courses.course_name
               FROM curriculum, curric_ops, courses
               WHERE curric_ops.op_for = curriculum.curric_name
               AND curric_ops.course_name = courses.course_name
               AND curriculum.curric_name = %s AND curriculum.person_id = %s
               GROUP BY courses.course_name"""

    #Create a dictionary of all the subjects in the level 1 topics
    lvl1Subjects = {}

    vals = (target['curric_name'], 1)

    mycursor.execute(topicSQL, vals)
    lvl1Units = mycursor.fetchall()

    #Get all the subjects for lvl 1 topics
    for K in lvl1Units:
        lvl1Subjects[K[0]] = 0
    #Get the units for each subject in lvl1 topics
    for M in lvl1Units:
        lvl1Subjects[M[0]] += M[1]

    #Get the hours for the required courses
    mycursor.execute(reqSQL, vals)
    reqHrs = mycursor.fetchall()
    #Get the hours for the optional courses
    mycursor.execute(opSQL, vals)
    opHrs = mycursor.fetchall()

    #Compare required hours with topic units
    for J in reqHrs:
        if J[0] in lvl1Subjects:
            lvl1Subjects[J[0]] -= J[1]

    #If the hours are positive for any subject, it is Substandard coverage
    for I, V in lvl1Subjects:
        if V > 0:
            return 'Substandard'

    #Now check if it has enough required hours for level 2 topics
    vals[1] = 2
    lvl2Subjects = {}

    mycursor.execute(topicSQL, vals)
    lvl2Units = mycursor.fetchall()

    #Populate lvl1 and lvl2 Subject maps
    for K in lvl1Units:
        lvl1Subjects[K[0]] = 0
    for M in lvl2Units:
        lvl2Subjects[M[0]] = 0
    for S in lvl1Units:
        lvl2Subjects[S[0]] += S[1]
    for G in lvl2Units:
        lvl2Subjects[G[0]] += G[1]

    leftReqs = {}
    for I in reqHrs:
        if I[0] in lvl1Subjects:
            leftReqs[I] = V-lvl1Subjects[I]

    for I, V in lvl2Subjects:
        if I not in leftReqs:
            return 'Unsatisfactory'

    for I, V in lvl2Subjects:
        if (leftReqs[I]) < (lvl2Subjects[I]*(target['min_cover2']/100)):
            return 'Unsatisfactory'

    #Find outif lvl 2 is fully covered by required courses or not
    l2Covered = True
    for I, V in lvl2Subjects:
        if leftReqs[I] < lvl2Subjects[I]:
            l2Covered = False
    if l2Covered:
        for I, V in leftReqs:
            if I in lvl2Subjects:
                leftReqs[I] -= lvl2Subjects[I]
        for J in opHrs:
            if J[0] in leftReqs:
                leftReqs[I] += opHrs[1]
        vals[1] = 3
        lvl3Subjects = {}
        mycursor.execute(topicSQL, vals)
        lvl3Units = mycursor.fetchall()
        for K in lvl3Units:
            if K[0] in lvl3Subjects:
                lvl3Subjects[K[0]] = 0
            else:
                lvl3Subjects[K[0]] += k[1]

        for I, V in lvl3Subjects:
            if I in leftReqs:
                if leftReqs[I] < (lvl3Subjects*(target['min_cover3']/100)):
                    return 'Inclusive'
            else:
                return 'Inclusive'
        return 'Extensive'

    else:
        for I, V in lvl2Subjects:
            if I not in opHrs:
                return 'Basic'
            if (leftReqs[I]+opHrs[I]) < lvl2Subjects[I]:
                return 'Basic'
        return 'Basic-Plus'
