## Insert data

def insert_into_curric( new_curric_data, mycursor, mydb):
    sql = """INSERT INTO curriculum
            (curric_name, person_name, person_id, min_hours, topic_cat)
            VALUES (%s, %s, %s, %s, %s)"""

    vals = (new_curric_data['curric_name'], new_curric_data['person_name'],
            new_curric_data['person_id'], new_curric_data['min_hours'], new_curric_data['topic_cat'])


    mycursor.execute(sql, vals)

    mydb.commit()

    print('\nThe ' + new_curric_data['curric_name'] + ' curriculum has been added.')
