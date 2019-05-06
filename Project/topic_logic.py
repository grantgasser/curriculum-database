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
#       target: A dictionary containing the primary key of the curriculum
#       mycursor: The cursor to execute the queries for information
#       mydb: The database in which the curriculum lies
#######################################################################################
def calcCat(target, mycursor, mydb):
    topicSQL = """SELECT topic.subject, topic.units, topic.topic_id, topic.topic_name
                  FROM curriculum, topic, topic_curric
                  WHERE topic_curric.topic_id = topic.topic_id
                  AND topic_curric.curric_assoc = curriculum.curric_name
                  AND curriculum.curric_name = %s AND curriculum.person_id = %s
                  AND topic.lvl = %s
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

    vals = (target['curric_name'], target['person_id'], 1)

    mycursor.execute(topicSQL, vals)
    lvl1Units = mycursor.fetchall()

    #Get all the subjects
    for K in lvl1Units:
        lvl1Subjects[K[0]] = 0
    #Get the units for each subject in lvl1 topics
    for M in lvl1Units:
        lvl1Subjects[M[0]] += M[1]
    
    #Get the hours for the required courses
    mycursor.execute(reqSQL, vals)
    reqHrs = mycursor.fetchall()

    #Compare required hours with topic units
    for J in reqHrs:
        lvl1Subjects[J[0]] -= J[1]

    #If the hours are positive for any subject, it is Substandard coverage
    for I, V in lvl1Subjects:
        if V > 0:
            return 'Substandard'


    



