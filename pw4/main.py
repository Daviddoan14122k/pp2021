
# import some package

import curses
import input
import output


# initial use screen curses
screen = curses.initscr()
curses.start_color()

   
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

# calculate gpa of student
calculation_Gpa()

screen.refresh()
screen.clear()
try:
    screen.addstr(0,5, "Do you want to see mark of all student ?")
    screen.addstr(1,5, "1. Yes")
    screen.addstr(2,5, "2. No \n")
except curses.error:
    pass
option = int(screen.getstr().decode())
if option == 1:
    screen.clear()
    screen.addstr("Hence, This is table mark of students")
    screen.refresh()
    screen.clear()
    curses.napms(3000)
    display_mark()
    screen.addstr("Hence, This is table mark of students after sort GPA descending: ")
    screen.refresh()
    curses.napms(3000)
    GPA_decending()
else:
    screen.addstr("say goodbye!!")
    curses.napms(2000)
    curses.endwin()
