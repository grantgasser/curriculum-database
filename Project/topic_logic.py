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

