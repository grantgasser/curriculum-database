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
			 FROM   sec_grades  
			 WHERE  section_id IN (SELECT DISTINCT section_id
								   FROM curric_reqs NATURAL JOIN curric_ops NATURAL JOIN section 
								   WHERE course_name = %s 
								   AND (op_for = %s OR req_for = %s) 
								   AND year BETWEEN %s AND %s)
			GROUP BY section_id
		 """

	vals = (curric_name,course_name,year1,year2)

	mycursor.execute(sql,vals)
	return mycursor.fetchall()

#-----------------------------QUERY POINT #4-------------------------------------------------

'''
	def get_curric_distr(curric_name,semester1,semester2,year,mycursor):
#query incomplete

	vals = (curric_name,semester1,semester2,year)
	mycursor.execute(sql,vals)
	mycursor.fetchall()
'''

#-------------------QUERY POINT #5-----------------------------------------------------------
def get_curric_dash(curric_name,mycursor):

	sql = """SELECT curric_name,person_name
		  	 FROM curriculum NATURAL JOIN curric_ops NATURAL JOIN curric_reqs
		  	 WHERE  curric_name = %s"""

	vals = (curric_name,)

	mycursor.execute(sql,vals)
	mycursor.fetchall(cntReq,cntOpt)

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
	mycursor.fetchall()
'''
def is_given_curric_goal_valid(curric_name,mycursor):



	vals = (curric_name,)

	mycursor.execute(sql,vals)
	mycursor.fetchall()
'''
