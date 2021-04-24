   
# import some package

import numpy as np
import curses

# Create all list to contain object
students = []
studentID = []
courses = []
courseID = []
Course_credit = []
marks = []
mark_detail = []
mark_gpa = []

# initial use screen curses
screen = curses.initscr()
curses.start_color()

class main_output():
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
                screen.addstr("CourseID: %s     CourseName: %s \n" % (c.get_id(), c.get_name()))
            except curses.error:
                pass
            screen.refresh()
        
    #function to display mark of student given the course
    def display_mark():
        for m in marks:
            try:
                screen.addstr("Mark_coursesid: %s     Mark_studentid: %s    Mark_mark: %s \n" % (m.get_cid(), m.get_sid(), m.get_mark()))
            except curses.error:
                pass
            screen.refresh()

    #function to sort GPA decending
    def GPA_decending():
        arr=np.array([mark_gpa])  
        arr[::-1].sort()
        screen.addstr("The list after sorting is %s: \n"%(arr))
        screen.refresh()