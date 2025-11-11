## COMP 3005 ASSIGNMENT 3
- **Name:** Bryan B.
- **Student Number:** 101277861

For this program, it will handle the basic operations described as: CRUD (create, read, update, destroy). One other function is used to connect to a specific database.

Using external library **psycopg2,** which handles connection to PostGreSQL databases, and has a variety of methods... in particular, using **queries** to send into the pSQL shell, and sometimes even commit/save new information.

### How to Run Program

Simply running this program directly will run all methods for testing:
- Printing all students in table in database
- Adding a example student into database
- Updating an email for a following student
- Deleting a student from the database

Which to directly run the program, simply do:
```
cd ...\assignment3
py CRUDapp.py
```
To use a specific function (replace following function with any other function):
```
cd ...\assignment3
py -c 'from CRUDapp import *; getAllStudents()'
```
