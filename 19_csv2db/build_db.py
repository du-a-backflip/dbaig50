# Dua Baig
# 45
# K19 SQL
# 2024-10-18

import csv
import sqlite3 #enable SQLite operations

DB_FILE="discobandit.db"
db = sqlite3.connect(DB_FILE) #open db if exists, otherwise create
c = db.cursor() #facilitate db ops

coursesExist = (c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='courses'").fetchall() == [])
if coursesExist: 
    command = "CREATE TABLE courses(code, mark, id)"
    c.execute(command) #makes the table with the three columns
    with open("courses.csv", newline="") as csvfile:
        coursesRaw = csv.DictReader(csvfile) #makes a dictionary out of the csv files (can be used to get values)
        for course in coursesRaw:
            command = f"INSERT INTO courses VALUES (?,?,?)"  #command to insert values
            # {course['code']}, {course['mark']}, {course['id']}
            val = (course['code'], course['mark'], course['id']) 
            c.execute(command, val) #val subs in for (?,?,?)

studentsExist = (c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='students'").fetchall() == []) #checks if student table exists (if not, creates a table)
if studentsExist:    
    command = "CREATE TABLE students (name, age, id)" #makes a tavle with the three columns
    c.execute(command)
    with open("students.csv", newline="") as csvfile:
        studentsRaw = csv.DictReader(csvfile) #makes dictionary out of csv file to get values from
        for student in studentsRaw:
            command = f"INSERT INTO students VALUES (?,?,?)"
            val = (student['name'], student['age'], student['id'])
            c.execute(command, val) #replaces (?,?,?) in command with value of val


db.commit() #save changes
for row in c.execute("SELECT id, code FROM courses"):
    print(row) #checks to see if everything added
print()
print()
for row in c.execute("SELECT id, name FROM students"):
    print(row)

db.close()
