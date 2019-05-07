## Get data (Queries)

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

def get_course(course_name, mycursor):
	sql = """SELECT  *
			 FROM courses
			 WHERE course_name = %s"""

	vals = (course_name,)

	req = get_reqs(course_name,mycursor)

	ops = get_ops(course_name,mycursor)

	mycursor.execute(sql,vals)
	return mycursor.fetchall(req,ops)


def get_reqs_given_course(course_name,mycursor):
	sql = """SELECT req_by
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

def get_section(curric_name,course_name,semester1,semester2,year, mycursor):

	sql = """SELECT *
			 FROM   sec_grades NATURAL JOIN section
			 WHERE  course_name = %s
			 AND semester BETWEEN %s AND %s
			 AND year = %s
			 AND course_name IN (SELECT course_name
			 					 FROM curric_reqs NATURAL JOIN curric_ops
			 					 WHERE op_for = %s OR req_by = %s)
		 """

	vals = (curric_name,course_name,semester1,semester2,year)

	mycursor.execute(sql,vals)
	return mycursor.fetchall();


def get_curric_dash(curric_name,mycursor):
#query incomplete
	sql = """SELECT curric_name,person_name,COUNT)
		  COUNT(DISTINCT curric_reqs.course_name),COUNT(DISTINCT curric_op.course_name),
		  	 FROM curriculum NATURAL JOIN curric_ops, NATURAL JOIN curric_reqs
		  	 WHERE  curric_name = %s"""

	cntReq = count_req_courses_for_curric(curric_name,mycursor)

	cntOpt = count_op_courses_for_curric(curric_name,mycursor)

	topCat = calcCat(curric_name,mycursor)

	vals = (curric_name)

	mycursor.execute(sql,vals)
	mycursor.fetchall(cntReq,cntOpt)

def count_req_courses_for_curric(curric_name,mycursor):
	sql = """SELECT COUNT(DISTINCT course_name)
	         FROM curric_reqs
	         WHERE req_for = %s """

	vals = (curric_name)

	mycursor.execute(sql,vals)
	return mycursor.fetchall()

def count_op_courses_for_curric(curric_name,mycursor):
	sql = """SELECT COUNT(DISTINCT course_name)
	         FROM curric_ops
	         WHERE op_for = %s """

	vals = (curric_name)

	mycursor.execute(sql,vals)
	return mycursor.fetchall()





'''
	def get_curric_distr(semester1,semester2,year,mycursor):
#query incomplete
	vals = (semester1,semester2,year)
	mycursor.execute(sql,vals)
	mycursor.fetchall()
'''
