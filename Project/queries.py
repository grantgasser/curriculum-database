
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

def get_course(course_name, mycursor):
	sql = """SELECT  * 
			 FROM courses
			 WHERE course_name = %s"""

	vals = (course_name)

	req = get_reqs(course_name,mycursor)

	ops = get_ops(course_name,mycursor)

	mycursor.execute(sql,vals)
	return mycursor.fetchall(req,ops)


def get_reqs(course_name,mycursor):
	sql = """SELECT req_by
	         FROM curric_reqs
	         WHERE course_name = %s """

	vals = (course_name)

	mycursor.execute(sql,vals)
	return mycursor.fetchall()

def get_ops(course_name,mycursor):
	sql = """SELECT op_for
	         FROM curric_reqs
	         WHERE course_name = %s """

	vals = (course_name)

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
			 
def get_curric_distr(semester1,semester2,year,mycursor):
#query incomplete  
	sql = """ """

	vals = (semester1,semester2,year)
	mycursor.execute(sql,vals)
	mycursor.fetchall()

def get_curric_dash(curric_name,mycursor):
#query incomplete
	sql = """SELECT curric_name,person_name,
		  COUNT(DISTINCT curric_reqs.course_name),COUNT(DISTINCT curric_op.course_name),
		  	 FROM curriculum NATURAL JOIN curric_ops, NATURAL JOIN curric_reqs
		  	 WHERE  curric_name = %s"""

	vals = (curric_name)

	mycursor.execute(sql,vals)
	mycursor.fetchall()
