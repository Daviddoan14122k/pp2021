# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 11:32:00 2021

@author: Doan Van Chuong
"""


# Create all list to contain dictionarys
students = []
studentID = []
courses = []
courseID = []
marks = []

# function to enter the number of students
def number_student():
    num = int(input("Enter the number of student in class: \n"))
    return num

# function to enter the number of courses
def number_course():
    num = int(input("Enter the number of courses in class: \n"))
    return num

#function to add student
def add_student():
    name = input("Enter student Name: ")
    id = input("Enter Student ID: ")
    DoB = input("Enter DoB Student: ")
    s = {'id':id,'name':name,'DoB':DoB}
    students.append(s)
    studentID.append(id)
    
#function to add course
def add_course():
    name = input("Enter the Name of Course: ")
    id = input("Enter Course ID: ")
    c = {'id':id,'name':name}
    courses.append(c)
    courseID.append(id)

#function choose corese to assign mark for student
def assign_mark():
    for i in range(0,len(courses)):
        C_id = input("Enter Course ID: ")
        if C_id in courseID:
            for j in range(0,len(students)):
                S_id = input("Enter Student ID: ")
                if S_id in studentID:
                    mark = float(input("Enter mark of Student: "))
                    m = {'S_id':S_id,'C_id':C_id,'mark':mark}
                else:
                    print("You enter wrong id of student")
                    break
                marks.append(m)
        else:
            print("You enter wrong id of course")
            break
      
#function to display students
def display_student():
    print("All student in class: ")
    for i in range(0,len(students)):
        print(f"id: {students[i]['id']}  name: {students[i]['name']}  DoB: {students[i]['DoB']}")

#function to display courses
def display_course():
    print("All course in class")
    for i in range(0,len(courses)):
        print(f"id: {courses[i]['id']}  name: {courses[i]['name']}")

#function to display mark of student given the course
def display_mark():
    for i in range(0,len(marks)):
        print(f"CourseID: {marks[i]['C_id']} \n +student have id: {marks[i]['S_id']} has {marks[i]['mark']} points")

#main function
# add student into students list
n = int(number_student())
for i in range(0,n):
    add_student()
display_student()

# add course into courses list
num = int(number_course())
for i in range(0,num):
    add_course()
display_course()

# choose course to enter the mark of student
assign_mark()

print("Do you want to see mark of all student ?")
for i in range(0,len(courses)):
    option = int(input("""
      1. yes
      2. no
      """))
    if option == 1:
        print("Hence, This is table mark of students")
        display_mark()
        break
    else:
        break