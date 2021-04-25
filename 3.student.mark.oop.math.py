# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 22:58:31 2021
@author: Doan Van Chuong
"""

# import some package

import math
import numpy as np
import curses

# Create all list to contain object
students = []
studentID = []
studentName = []
studentDoB = []

courses = []
courseID = []
course_Credit = []
courseName = []

marks = []
mark_detail = []
mark_gpa = []


# initial use screen curses
screen = curses.initscr()
curses.start_color()

#----------------------------- Students -----------------------------#
class Student:
    def __init__(self, id, name, DoB):
        self.id = id
        self.name = name
        self.DoB = DoB
        
    def get_id(self):
        return self.id 
    
    def get_name(self):
        return self.name
    
    def get_DoB(self):
        return self.DoB
    
    
#----------------------------- Courses -----------------------------#
class Course:
    def __init__(self, id, name, credit):
        self.id = id
        self.name = name
        self.credit = credit
        
        
    def get_id(self):
        return self.id 
    
    def get_name(self):
        return self.name
    
    def get_credit(self):
        return self.credit        


#----------------------------- Marks -----------------------------#
class Mark:
    def __init__(self, s_id, c_id, mark, gpa=0):
        self.s_id = s_id
        self.c_id = c_id
        self.mark = mark
        self.gpa = gpa
      
    
    def get_cid(self):
        return self.c_id 
    
    def get_sid(self):
        return self.s_id
    
    def get_mark(self):
        return self.mark
    
    def get_gpa(self):
        return self.gpa
    
    def set_gpa(self, gpa):
        self.gpa = gpa
    
# function to enter the number of students
def number_student():
    while True:
        screen.addstr("Enter the number of students in class:")
        screen.refresh()
        Num=int(screen.getstr().decode())
        if Num <=0:
            curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
            screen.addstr("Does not exits!!!\n", curses.color_pair(1))
            screen.refresh()
            curses.napms(3000)
            screen.clear()
            screen.refresh()
        else:
            return Num
             
             
# function to enter the number of courses
def number_course():
    while True:
        screen.addstr("Enter the number of courses in class:")
        screen.refresh()
        Nums=int(screen.getstr().decode())
        if Nums <=0:
            curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
            screen.addstr("Does not exits!!!\n", curses.color_pair(1))
            screen.refresh()
            curses.napms(3000)
            screen.clear()
            screen.refresh()
        else:
            return Nums
      
#function to add student
def add_student():
    screen.addstr("Enter Student ID: ")
    screen.refresh()
    id = screen.getstr().decode()
    
    screen.addstr("Enter student Name: ")
    screen.refresh()
    name = screen.getstr().decode()

    screen.addstr("Enter DoB Student: ")
    screen.refresh()
    DoB = screen.getstr().decode()
    
    s = Student(id,name,DoB)
    students.append(s)
    studentID.append(id)
    studentName.append(name)
    screen.refresh()
    screen.clear()
  
    
#function to add course
def add_course():
    screen.addstr("Enter Course ID: ")
    screen.refresh()
    id = screen.getstr().decode()
    
    screen.addstr("Enter the Name of Course: ")
    screen.refresh()
    name = screen.getstr().decode()  

    screen.addstr("Enter Credit of Course: ")
    screen.refresh()
    credit = float(screen.getstr().decode())
    
    c = Course(id,name,credit)
    courses.append(c)
    courseID.append(id)
    courseName.append(name)
    course_Credit.append(credit)
    screen.refresh()
    screen.clear()


#function choose corese to assign mark for student
def assign_mark():
    screen.addstr("Enter the courseID you want to input mark: ")
    c_id = (screen.getstr().decode())
    screen.clear()
    screen.refresh()
    if c_id in courseID:
        screen.addstr("Enter the StudentID you want to input mark: ")
        s_id=screen.getstr().decode()
        screen.clear()
        screen.refresh()
        if s_id in studentID:   
            while True:           
                screen.addstr("Enter mark of this student in courses: ")
                mark=math.floor(float(screen.getstr().decode()))
                if mark<0 or mark>20:
                    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
                    try:
                        screen.addstr("Error!!!\n", curses.color_pair(1))
                    except curses.error:
                            pass
                    screen.refresh()
                    curses.napms(1000)
                    screen.clear()
                    screen.refresh()
                    screen.addstr("Please enter number in range (0,20): \n")
                    mark=math.floor(float(screen.getstr().decode()))
                else:
                    break  
        else:
            exit()
    else:
        exit() 
    mark_detail.append(mark)
    m = Mark(s_id,c_id,mark)
    marks.append(m)
    
# function to assign gpa in mark list
def calculation_Gpa():     
    value=np.array([mark_detail])
    points=np.array([course_Credit])
    screen.addstr("Enter studentID you want to calculate gpa:")
    id =screen.getstr().decode()
    if id in studentID:
        for i in range(len(marks)):
            totalCredit=np.sum(points)
            totalValue=np.sum(np.multiply(value,points))
            screen.refresh()
            gpa = totalValue/totalCredit
            screen.refresh()                
    else: 
        return 0
    mark_gpa.append(gpa)
    screen.refresh()
    for m in marks:
        screen.clear()
        screen.refresh()
        screen.addstr(" [Mark_studentID: ] %s   [Gpa: ]%s \n" %(m.get_cid(), gpa))
        screen.refresh()
        break
    
#function to display students
def display_student():
    screen.addstr("All students in class: \n")
    screen.refresh()
    for s in students:
        try:
            screen.addstr("StudentID: %s     StudentName: %s     StudentDoB: %s\n" % (s.get_id(), s.get_name(), s.get_DoB()))
        except curses.error:
            pass
        screen.refresh()

#function to display courses
def display_course():
    screen.addstr("All courses in class: \n")
    screen.refresh()
    for c in courses:
        try:
            screen.addstr("CourseID: %s     CourseName: %s    CourseCređit: %s\n" % (c.get_id(), c.get_name(), c.get_credit()))
        except curses.error:
            pass
        screen.refresh()
    
#function to display mark of student given the course
def display_mark():
    for m in marks:
        try:
            screen.addstr("CourseID: %s     StudentID: %s    Mark_detail: %s \n" % (m.get_cid(), m.get_sid(), m.get_mark()))
        except curses.error:
            pass
        screen.refresh()
        
#function to sort GPA decending
def GPA_decending():
    arr=np.array([mark_gpa])  
    arr[::-1].sort()
    screen.addstr("The list after sorting is %s: \n"%(arr))
    screen.refresh()


#main function
def main():
    screen.refresh()
    screen.clear()
    try:
        screen.addstr(0,5, "Do you want to input student and courses ?")
        screen.addstr(1,5, "1. Yes")
        screen.addstr(2,5, "2. No \n")
    except curses.error:
        pass
    option1 = int(screen.getstr().decode()) 
    while True:
        if option1 == 1:
            screen.clear()
            N_co = int(number_course())
            screen.clear()
            screen.refresh()
            for i in range (N_co):
                screen.addstr(f"Course {i+1} \n")
                add_course()
                screen.refresh()
                N_st = int(number_student())
                screen.refresh()
                screen.clear()
                for i in range (N_st):
                    screen.addstr(f"Student {i+1} \n")
                    add_student()
                    screen.refresh()
                    screen.clear()
                    assign_mark()
                    screen.clear()
                    screen.refresh()
            break
        else:
            screen.addstr("say goodbye!!")
            curses.napms(2000)
            curses.endwin()
            exit()
            
    screen.refresh()
    screen.clear()
    try:
        screen.addstr(0,5, "Do you want to calculater GPA of student ?")
        screen.addstr(1,5, "1. Yes")
        screen.addstr(2,5, "2. No \n")
    except curses.error:
        pass
    option2 = int(screen.getstr().decode())
    if option2 == 1:
        screen.refresh()
        calculation_Gpa()
        curses.napms(2000)
        screen.clear()
        screen.refresh()
    else:
        screen.addstr("say goodbye!!")
        curses.napms(2000)
        curses.endwin()
    
    while True:
        screen.addstr("1. Display list of Students: \n")
        screen.addstr("2. Display list of Courses: \n") 
        screen.addstr("3. Display marks \n")
        screen.addstr("4. GPA_descending \n")
        screen.addstr("5. Stop \n")
        option3 = int(screen.getstr().decode())
        screen.refresh()
        screen.clear()
        screen.refresh()
        if option3 == 1:
            display_student()
        if option3 == 2:
            display_course()
        if option3 == 3:
            display_mark()
        if option3 == 4:
            GPA_decending()
        elif option3 == 5:
            screen.addstr("  Good bye,see you again\n  ")
            screen.refresh()
            curses.napms(1000)
            curses.endwin()
            exit()  
if __name__ == '__main__':
    main()
    
