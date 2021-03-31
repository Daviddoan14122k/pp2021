# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 22:58:31 2021

@author: Doan Van Chuong
"""

# Create all list to contain object
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


# define object student,course
class Student:
    def __init__(self, id, name, DoB):
        self.id = id
        self.name = name
        self.DoB = DoB
    
    def display(self):
        print(f"id: {self.id}  name: {self.name}  DoB: {self.DoB}")
    
class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def display(self):
        print(f"id: {self.id}  name: {self.name}")

class Mark:
    def __init__(self, s_id, c_id, mark):
        self.s_id = s_id
        self.c_id = c_id
        self.mark = mark
    
    def display(self):
        print(f"CourseID: {self.c_id} \n + student have id: {self.s_id} has {self.mark} points")
        
        
#function to add student
def add_student():
    id = input("Enter Student ID: ")
    name = input("Enter student Name: ")
    DoB = input("Enter DoB Student: ")
    s = Student(id,name,DoB)
    students.append(s)
    studentID.append(id)
    
#function to add course
def add_course():
    id = input("Enter Course ID: ")
    name = input("Enter the Name of Course: ")
    c = Course(id,name)
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
                    m = Mark(S_id,S_id,mark)
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
        Student.display(students[i])

#function to display courses
def display_course():
    print("All course in class")
    for i in range(0,len(courses)):
        Course.display(courses[i])
    
#function to display mark of student given the course
def display_mark():
    for i in range(0,len(marks)):
        Mark.display(marks[i])


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