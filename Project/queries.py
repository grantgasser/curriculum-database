#############################################################################################
# Authors: Zee Dugar, Grant Gasser, Jackson O'Donnell
#
# Purpose: Host the functions to obtain data from the database for the user
#############################################################################################

import topic_logic as tl

## Get data (Queries)
#---------------------------QUERY POINT #1---------------------------------------------------
#get curriculum
#arguments: key of the table (curric_name, person_id) and the sql cursor
def get_curric(curric_name, person_id, mycursor):
    sql = """SELECT *
    		 FROM curriculum
    		 WHERE curric_name = %s
             AND person_id = %s"""
    vals = (curric_name, person_id)

    mycursor.execute(sql,vals)
    return mycursor.fetchall()

#get topic given curriculum name (first bullet point on queries)
def get_topic_curric(curric_assoc, mycursor):
    sql = """SELECT topic_name
            FROM topic, topic_curric
            WHERE topic.topic_id = topic_curric.topic_id
            AND curric_assoc = %s"""

    vals = (curric_assoc,)

    mycursor.execute(sql, vals)
    return mycursor.fetchall()

#gets required courses given a curric_name
def get_reqs_given_curric(curric_name, mycursor):
    sql = """SELECT course_name
            FROM curric_reqs
            WHERE req_for = %s"""
    vals = (curric_name,)

    mycursor.execute(sql, vals)
    return mycursor.fetchall()

#gets optional courses given a curric_name
def get_ops_given_curric(curric_name, mycursor):
    sql = """SELECT course_name
            FROM curric_ops
            WHERE op_for = %s"""
    vals = (curric_name,)

    mycursor.execute(sql, vals)
    return mycursor.fetchall()
#---------------------------QUERY POINT #2---------------------------------------------------
#gets course tuple given course_name
def get_course(course_name, mycursor):
	sql = """SELECT  *
			 FROM courses
			 WHERE course_name = %s"""

	vals = (course_name,)

	mycursor.execute(sql,vals)
	return mycursor.fetchall()


def get_reqs_given_course(course_name,mycursor):
	sql = """SELECT req_for
	         FROM curric_reqs
	         WHERE course_name = %s """

	vals = (course_name,)

	mycursor.execute(sql,vals)
	return mycursor.fetchall()

def get_ops_given_course(course_name,mycursor):
	sql = """SELECT op_for
	         FROM curric_ops
	         WHERE course_name = %s """

	vals = (course_name,)

	mycursor.execute(sql,vals)
	return mycursor.fetchall()

#---------------------------QUERY POINT #3---------------------------------------------------

def get_section(curric_name,course_name,year1,year2, mycursor):

	sql = """SELECT *
FROM sec_grades
WHERE sec_grades.section_id IN (SELECT section.section_id
					 FROM section JOIN curric_reqs JOIN curric_ops
                     WHERE req_for = %s OR op_for = %s
					AND year BETWEEN %s AND %s
					AND section.course_name = %s)
GROUP BY section_id;
		 """

	vals = (curric_name,curric_name,year1,year2,course_name)

	mycursor.execute(sql,vals)
	return mycursor.fetchall()

#-----------------------------QUERY POINT #4-------------------------------------------------

#############################################################################################
# Function: get_curric_distro
#
# Purpose: For each curriculum and a given semester range, output the aggregate distribution
#       of each outcome.
#
# Parameters:
#       curric_name: The name of the curriculum
#       times: A list of two years followed by up to four semesters (blank if no semster chosen)
#       mycursor: The cursor to query with
#############################################################################################
def get_curric_distro(curric_name, times, mycursor):
    sql = """SELECT curriculum.curric_name, SUM(`A+`), SUM(A), SUM(`A-`),
                                            SUM(`B+`), SUM(A), SUM(`B-`),
                                            SUM(`C+`), SUM(A), SUM(`C-`),
                                            SUM(`D+`), SUM(A), SUM(`D-`),
                                            SUM(F), SUM(I), SUM(W)
             FROM curriculum, curric_ops, curric_reqs, section, sec_grades
             WHERE (curriculum.curric_name = curric_ops.op_for
               OR curriculum.curric_name = curric_reqs.req_for)
               AND (section.course_name = curric_ops.course_name
               OR section.course_name = curric_reqs.course_name)
               AND section.section_id = sec_grades.section_id
               AND (section.year >= %s OR section.year <= %s)
               AND ("""
    for I in range(2, len(times)):
        if times[2] != '':
            sql += "section.semseter = %s OR "
    sql = sql[0:-3]

    mycursor.execute(sql, times)
    return mycursor.fetchall()



#-------------------QUERY POINT #5-----------------------------------------------------------
def get_curric_dash(curric_name,mycursor):

	sql = """SELECT curric_name,person_name
		  	 FROM curriculum NATURAL JOIN curric_ops NATURAL JOIN curric_reqs
		  	 WHERE  curric_name = %s"""

	vals = (curric_name,)

	mycursor.execute(sql,vals)
	return mycursor.fetchall(cntReq,cntOpt)

def count_req_courses_given_curric(curric_name,mycursor):

	sql = """SELECT COUNT(DISTINCT course_name)
	         FROM curric_reqs
	         WHERE req_for = %s """

	vals = (curric_name,)

	mycursor.execute(sql,vals)
	return mycursor.fetchall()

def count_op_courses_given_curric(curric_name,mycursor):
	sql = """SELECT COUNT(DISTINCT course_name)
	         FROM curric_ops
	         WHERE op_for = %s """

	vals = (curric_name,)

	mycursor.execute(sql,vals)
	return mycursor.fetchall()


def count_total_credits_given_curric(curric_name,mycursor):
	sql = """SELECT SUM(cred_hrs)
	         FROM courses
	         WHERE course_name IN (SELECT DISTINCT course_name
	         						FROM curric_ops NATURAL JOIN curric_reqs
	         						WHERE req_for = %s OR op_for = %s) """

	vals = (curric_name,)

	mycursor.execute(sql,vals)
	return mycursor.fetchall()

def count_levels_given_curric(curric_name,mycursor):
	sql = """SELECT COUNT(lvl)
			 FROM topic NATURAL JOIN topic_curric
			 WHERE curric_assoc = %s"""

	vals = (curric_name,)

	mycursor.execute(sql,vals)
	return mycursor.fetchall()

def min_hours_given_curric(curric_name,mycursor):
	sql = """SELECT min_hours,min_cover2,min_cover3
		   FROM curriculum
		   WHERE curric_name = %s """
	vals = (curric_name,)

	mycursor.execute(sql,vals)
	return mycursor.fetchall()

def get_creds_for_course_goals(curric_name,mycursor):

	sql = """SELECT SUM(cred_hrs)
			 FROM courses NATURAL JOIN course_goals
			 WHERE goal_id IN (SELECT goal_id
				  			   FROM goals
                  			   WHERE curric_name = %s)"""

	vals = (curric_name,)

	mycursor.execute(sql,vals)
	return mycursor.fetchall()

def get_goal_hrs_given_curric(curric_name,mycusor):

 	sql = """SELECT (goal_hrs)
 			 FROM goals
 			 WHERE curric_name = %s"""

 	vals = (curric_name,)


def is_curric_goal_valid(curric_name,mycursor):

	if get_goal_hrs_given_curric(curric_name,mycursor) >= get_creds_for_course_goals(curric_name,mycursor):
		print("NOT GOAL VALID")
	else:
		print("GOAL VALID")

# Use the topic logic function to get the topic category
def get_curric_topic_category(curric_name, mycursor):
    vals = (curric_name,)
    mycursor.execute("""SELECT min_cover2, min_cover3 FROM curriculum
                        WHERE curric_name = %s""", vals)
    covers = mycursor.fetchall()
    target = {'curric_name': curric_name,
              'min_cover2': covers[0][1],
              'min_cover3': covers[0][2]}

    category = tl.calcCat(target, mycursor)
    if category == 'Substandard':
        print("SUBSTANDARD COVERAGE")
    elif category == 'Unsatisfactory':
        print("UNSATISFACTORY COVERAGE")
    elif category == 'Inclusive':
        print("INCLUSIVE COVERAGE")
    elif category == 'Extensive':
        print("EXTENSIVE COVERAGE")
    elif category == 'Basic':
        print("BASIC COVERAGE")
    elif category == 'Basic-Plus':
        print("BASIC-PLUS COVERAGE")
