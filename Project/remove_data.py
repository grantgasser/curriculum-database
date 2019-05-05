#################################################################################
# Author: Jackson O'Donnell
#
# Purpose: A set of functions to allow the user to remove data from the database
#
#################################################################################


#################################################################################
# Function: removeCurriculum
# 
# Purpose: Remove a curriculum from the database entirely
#
# Parameters:
#       mycursor: The cursor to execute the deletions
#       mydb: The database in which the table lies
#       target: A dictionary containing the primary key of the item to be removed
################################################################################
def removeCurriculum(mycursor, mydb, target):
    sql = """DELETE FROM curriculum WHERE curric_name = %s 
                  AND person_id = %s"""

    vals = (target['curric_name'], target['person_id'])

    mycursor.execute(sql, vals)
    mydb.commit()

    print('\nThe curriculum '+target['curric_name']+' was removed')
