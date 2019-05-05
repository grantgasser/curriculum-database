
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
	sql = """SELECT  courses.course_name,* 
			 FROM courses, curric_ops, curric_reqs
			 WHERE courses.course_name = %s
			 AND courses.course_name = curric_ops.course_name
			 AND courses.course_name = curric_reqs.course_name
			 GROUP BY courses.course_name
			 """

	vals = (course_name)

	mycursor.execute(sql,vals)
	return mycursor.fetchall()


def get_section(course_name,curric_name,semester,year1, year2, mycursor):

	sql = """SELECT course_name
			 FROM curric_reqs NATURAL JOIN curric_ops
			 WHERE course_name = %s
			 AND (req_for = %s
			 OR req_opt = %s)
			 AND course_name IN (
			 	SELECT course_name, *
			 	FROM section RIGHT JOIN sec_grades
			 	WHERE course_name = section.course_name
				AND semester = %s 
				AND year BETWEEN %s AND %s
				AND sec_grades.section_id = section.section_id )
			 """
			 
	vals = (course_name,curric_name,semester,year1,year2)

	mycursor.execute(sql,vals)
	return mycursor.fetchall()



