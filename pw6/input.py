import math
import curses
import numpy as np
from domain.Student import *
from domain.Course import *
from domain.Mark import *

# initial use screen curses
screen = curses.initscr()
curses.start_color()

class main_in():
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
        