####################################################################################
# Author: Jackson O'Donnell
#
# Purpose: Functions to update data in the tables
####################################################################################

####################################################################################
# Function: updateCurriculum 
#
# Purpose: updates the curriculum table
#
# Parameters:
#        curric: A dictionary containing the primary key for the curriculum to edit
#        mycursor: A cursor to do the updates
#        mydb: The database in which the table lies
####################################################################################
def updateCurriculum( curric, mycursor, mydb):
    attr = input("""What attribute would you like to change? (curriculum = name of the curriculum
                                                       name = name of the instructor
                                                       id = id of the instructor
                                                       hours = the minimum hour requirements)"""
    
    new_data = {}
    if attr == "curriculum"
        attr = "curric_name"
        new_data['curric_name'] = input("Change the curriculum's name to: ")
    elif attr == "name"
        attr = "person_name"
        new_data['person_name'] = input("Change the instructor's name to: ")
    elif attr == "id"
        attr = "person_id"
        new_data['person_id'] = input("Change the ID of the instructor to: ")
    elif attr == "hours"
        attr = "min_hours"
        new_data['min_hours'] = input("Change the minimum hour requirement to: ")

    print("What would you like to change the attribute to?\n")
    sql = """UPDATE curriculum SET """+attr+""" = %s
             WHERE curric_name = %s AND person_id = %s""" 

    vals = (new_data[attr], target['curric_name'], target['person_id'])

    mycursor.execute(sql, vals)

    mydb.commit()

    print('\nThe curriculum has been updated')


##################################################################################
# Function: insert_into_courses
# 
# Purpose: Insert data into the courses table of the database
# 
# Parameters:
#        new_data: A dictionary of the data to be inserted
#        mycursor: A cursor to do the insertions
#        mydb: The database in which the table lies
##################################################################################
def insert_into_courses(new_data, mycursor, mydb):
    sql = """INSERT INTO courses (course_name, subj_code, course_no, cred_hrs, description)
             VALUES (%s, %s, %s, %s, %s);"""

    vals = (new_data['course_name'], new_data['subj_code'], new_data['course_no'],
            new_data['cred_hrs'], new_data['description'])

    mycursor.execute(sql, vals)

    mydb.commit()

    print('\nThe ' + new_data['course_name'] + ' course has been added.')


##################################################################################
# Function: insert_into_reqs
# 
# Purpose: Insert data into the curric_reqs table of the database
# 
# Parameters:
#        new_data: A dictionary of the data to be inserted
#        mycursor: A cursor to do the insertions
#        mydb: The database in which the table lies
##################################################################################
def insert_into_reqs(new_data, mycursor, mydb):
    sql = """INSERT INTO curric_reqs (course_name, req_for)
             VALUES (%s, %s);"""

    vals = (new_data['course_name'], new_data['req_for'])

    mycursor.execute(sql, vals)

    mydb.commit()

    print('\nThe new course requirement has been added.')


##################################################################################
# Function: insert_into_ops
# 
# Purpose: Insert data into the curric_ops table of the database
# 
# Parameters:
#        new_data: A dictionary of the data to be inserted
#        mycursor: A cursor to do the insertions
#        mydb: The database in which the table lies
##################################################################################
def insert_into_ops(new_data, mycursor, mydb):
    sql = """INSERT INTO curric_ops (course_name, op_for)
             VALUES (%s, %s);"""

    vals = (new_data['course_name'], new_data['op_for'])

    mycursor.execute(sql, vals)

    mydb.commit()

    print('\nThe new course option has been added.')


##################################################################################
# Function: insert_into_topic
# 
# Purpose: Insert data into the topic table of the database
# 
# Parameters:
#        new_data: A dictionary of the data to be inserted
#        mycursor: A cursor to do the insertions
#        mydb: The database in which the table lies
##################################################################################
def insert_into_topic(new_data, mycursor, mydb):
    sql = """INSERT INTO topic (topic_id, topic_name, lvl, subject, units)
             VALUES (%s, %s, %s, %s, %s);"""

    vals = (new_data['topic_id'], new_data['topic_name'], new_data['lvl'],
            new_data['subject'], new_data['units'])

    mycursor.execute(sql, vals)

    mydb.commit()

    print('\nThe ' + new_data['topic_name'] + ' topic has been added.')


##################################################################################
# Function: insert_into_topic_curric
# 
# Purpose: Insert data into the topic_curric table of the database
# 
# Parameters:
#        new_data: A dictionary of the data to be inserted
#        mycursor: A cursor to do the insertions
#        mydb: The database in which the table lies
##################################################################################
def insert_into_topic_curric(new_data, mycursor, mydb):
    sql = """INSERT INTO topic_curric (topic_id, curric_assoc)
             VALUES (%s, %s);"""

    vals = (new_data['topic_id'], new_data['curric_assoc'])

    mycursor.execute(sql, vals)

    mydb.commit()

    print('\nThe new topic-curriculum association has been added.')


##################################################################################
# Function: insert_into_goals
# 
# Purpose: Insert data into the goals table of the database
# 
# Parameters:
#        new_data: A dictionary of the data to be inserted
#        mycursor: A cursor to do the insertions
#        mydb: The database in which the table lies
##################################################################################
def insert_into_goals(new_data, mycursor, mydb):
    sql = """INSERT INTO goals(goal_id, description, curric_name)
             VALUES (%s, %s, %s);"""

    vals = (new_data['goal_id'], new_data['description'], new_data['curric_name'])

    mycursor.execute(sql, vals)

    mydb.commit()

    print('\nThe new goal has been added.')


##################################################################################
# Function: insert_into_section
# 
# Purpose: Insert data into the section table of the database
# 
# Parameters:
#        new_data: A dictionary of the data to be inserted
#        mycursor: A cursor to do the insertions
#        mydb: The database in which the table lies
##################################################################################
def insert_into_section(new_data, mycursor, mydb):
    sql = """INSERT INTO section (section_id, course_name, semester, num_stu, comment1, comment2)
             VALUES (%s, %s, %s, %s, %s, %s);"""

    vals = (new_data['section_id'], new_data['course_name'], new_data['semester'],
            new_data['num_stu'], new_data['comment1'], new_data['comment2'])

    mycursor.execute(sql, vals)

    mydb.commit()

    print('\nThe new section of course ' + new_data['course_name'] + ' has been added.')


##################################################################################
# Function: insert_into_sec_grades
# 
# Purpose: Insert data into the sec_grades table of the database
# 
# Parameters:
#        new_data: A dictionary of the data to be inserted
#        mycursor: A cursor to do the insertions
#        mydb: The database in which the table lies
##################################################################################
def insert_into_sec_grades(new_data, mycursor, mydb):
    sql = """INSERT INTO sec_grades (section_id, A+, A, A-, B+, B, B-, C+, C, C-, D+, D, D-, F, I, W)
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""" 

    vals = (new_data['section_id'], new_data['A+'], new_data['A'], new_data['A-'], new_data['B+'],
            new_data['B'], new_data['B-'], new_data['C+'], new_data['C'], new_data['C-'],
            new_data['D+'], new_data['D'], new_data['D-'], new_data['F'], new_data['I'], new_data['W'])

    mycursor.execute(sql, vals)

    mydb.commit()

    print('\nThe new grade distribution has been added. Section id: '+new_data['section_id'])

##################################################################################
# Function: insert_into_goal_grades
# 
# Purpose: Insert data into the goal_grades table of the database
# 
# Parameters:
#        new_data: A dictionary of the data to be inserted
#        mycursor: A cursor to do the insertions
#        mydb: The database in which the table lies
##################################################################################
def insert_into_goal_grades(new_data, mycursor, mydb):
    sql = """INSERT INTO goal_grades (goal_id, A+, A, A-, B+, B, B-, C+, C, C-, D+, D, D-, F, I, W)
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""" 

    vals = (new_data['goal_id'], new_data['A+'], new_data['A'], new_data['A-'], new_data['B+'],
            new_data['B'], new_data['B-'], new_data['C+'], new_data['C'], new_data['C-'],
            new_data['D+'], new_data['D'], new_data['D-'], new_data['F'], new_data['I'], new_data['W'])

    mycursor.execute(sql, vals)

    mydb.commit()

    print('\nThe new grade distribution has been added. Goal id: '+new_data['section_id'])

##################################################################################
# Function: insert_into_course_goals
# 
# Purpose: Insert data into the course_goals table of the database
# 
# Parameters:
#        new_data: A dictionary of the data to be inserted
#        mycursor: A cursor to do the insertions
#        mydb: The database in which the table lies
##################################################################################
def insert_into_course_goals(new_data, mycursor, mydb):
    sql = """INSERT INTO course_goals (course_name, goal_id)
             VALUES (%s, %s);"""

    vals = (new_data['course_name'], new_data['goal_id'])

    mycursor.execute(sql, vals)

    mydb.commit()

    print('\nThe goal with id '+new_data['goal_id']+' has been added to the course '+new_data['course_name']+'.')

