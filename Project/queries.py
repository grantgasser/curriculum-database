## Get data (Queries)

#get curriculum
#arguments: key of the table (curric_name, person_id) and the sql cursor
def get_curric(curric_name, person_id, mycursor):
    sql = """SELECT * FROM curriculum WHERE curric_name = %s
                AND person_id = %s"""
    vals = (curric_name, person_id)

    mycursor.execute(sql,vals)
    return mycursor.fetchall()
