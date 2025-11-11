# Time to re-learn Python...
import psycopg2
from psycopg2 import sql

# sort of like 2804: connecting server thru parameters
# except i dont wanna use JS lol
def connect():
    return psycopg2.connect(
        dbname="university",
        user="postgres",
        password="1234", # WOULD BE MY PASSWORD BUT ISN'T. USE YOUR OWN PLEASE...
        host="localhost",
        port="5432" # default postgres port
    )

""" 
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name  TEXT NOT NULL,
    email      TEXT NOT NULL UNIQUE,
    enrollment_date DATE
);

INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');
"""

# CRUD FUNCTIONS ->
# simple get, with for loop
def getAllStudents():
    # connect w db
    connected = connect();
    cursor = connected.cursor();

    cursor.execute("SELECT * FROM Students;");
    students = cursor.fetchall();
    for i in students:
        print(i);

    # close up
    cursor.close();
    connected.close();

# using actual query with py formatting
def addStudent(first_name, last_name, email, enrollment_date):
    # connect w db
    connected = connect();
    cursor = connected.cursor();

    # we won't know if it works but we can catch errors with psycopg2
    try:
        # multi-line string to insert for execution
        cursor.execute("""
            INSERT INTO students (first_name, last_name, email, enrollment_date)
            VALUES (%s, %s, %s, %s);
            """, (first_name, last_name, email, enrollment_date));
        connected.commit(); # save changes
        print(f"SUCCESSFULLY ADDED: {first_name} {last_name}")
    except psycopg2.Error as e:
        print("ERROR WITH ADDING:", e);
    finally:
        # close up (will run regardless of try/except outcome)
        cursor.close();
        connected.close();

# again with query formatting but with a few more checks
def updateStudentEmail(student_id, new_email):
    # connect w db
    connected = connect();
    cursor = connected.cursor();

    try:
        # update table, make new email variable to replace where studentid is
        cursor.execute("""
            UPDATE students
            SET email = %s
            WHERE student_id = %s;
            """, (new_email, student_id));
        # must check if student exists...
        if cursor.rowcount == 0:
            print(f"STUDENT ID {student_id} NOT FOUND, RETURNING");
        else:
            connected.commit(); # save changes
            print(f"SUCCESSFULLY UPDATED STUDENT ID {student_id} EMAIL TO: {new_email}");
    except psycopg2.Error as e:
        print("ERROR WITH UPDATING:", e);
    finally:
        # close up
        cursor.close();
        connected.close();

# editting the table with a chance of not finding student
def deleteStudent(student_id):
    # connect w db
    connected = connect();
    cursor = connected.cursor();

    try:
        # single line, only matching with student id
        # student id, then nothing for index for para after
        cursor.execute("DELETE FROM students WHERE student_id = %s;", (student_id,));
        # must check if student exists...
        if cursor.rowcount == 0:
            print(f"STUDENT ID {student_id} NOT FOUND, RETURNING");
        else:
            connected.commit(); # save changes
            print(f"SUCCESSFULLY DELETED STUDENT ID {student_id} EMAIL");
    except psycopg2.Error as e:
        print("ERROR WITH DELETING:", e);
    finally:
        # close up
        cursor.close();
        connected.close();

# runs last if file is run directly
if __name__ == "__main__":
    # display all students, add one student, update another, delete student, print again
    getAllStudents()
    addStudent("Alice", "Johnson", "alice.johnson@example.com", "2023-09-03")
    updateStudentEmail(1, "john.newemail@example.com")
    deleteStudent(3)

    getAllStudents()
