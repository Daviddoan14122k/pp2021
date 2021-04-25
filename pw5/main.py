
import curses
from zipfile import ZipFile
import os
import zipfile
from output import main_out
from input import main_in
from domain.Student import *
from domain.Course import *
from domain.Mark import *


# initial use screen curses
screen = curses.initscr()
curses.start_color()

 
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
            N_co = int(main_in.number_course())
            screen.clear()
            screen.refresh()
            for i in range (N_co):
                screen.addstr(f"Course {i+1} \n")
                main_in.add_course()
                screen.refresh()
                N_st = int(main_in.number_student())
                screen.refresh()
                screen.clear()
                for i in range (N_st):
                    screen.addstr(f"Student {i+1} \n")
                    main_in.add_student()
                    screen.refresh()
                    screen.clear()
                    main_in.assign_mark()
                    screen.clear()
                    screen.refresh()
            break
        else:
            screen.addstr("say goodbye!!")
            curses.napms(2000)
            curses.endwin()
            file_list = ['Students.txt', 'Courses.txt', 'Marks.txt']
            with ZipFile('students.dat', 'w') as new_zip:
                for file_Name in file_list:
                    new_zip.write(file_Name)
                for file_Name in file_list:
                    os.remove(file_Name)
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
        main_in.calculation_Gpa()
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
        screen.addstr("5. Stop and compress file \n")
        screen.addstr("6. Decompress and load file \n")
        screen.addstr("7. Stop \n")
        option3 = int(screen.getstr().decode())
        screen.refresh()
        screen.clear()
        screen.refresh()
        if option3 == 1:
            main_out.display_student()
        if option3 == 2:
            main_out.display_course()
        if option3 == 3:
            main_out.display_mark()
        if option3 == 4:
            main_out.GPA_decending()
        if option3 == 5:
            file_list = ['Students.txt', 'Courses.txt', 'Marks.txt']
            with ZipFile('students.dat', 'w') as new_zip:
                for file_Name in file_list:
                    new_zip.write(file_Name)
                for file_Name in file_list:
                    os.remove(file_Name)
        if option3 == 6:
            if os.path.isfile('students.dat'):
                screen.addstr("This file students.dat exits \n")
                zip_file = ZipFile('students.dat','r')
                zip_file.extractall()
                if os.path.isfile('Students.txt'):
                    f = open('Students.txt','r')
                    f.readline()
                if os.path.isfile('Courses.txt'):
                    f = open('Courses.txt','r')
                    f.readline()
                if os.path.isfile('Marks.txt'):
                    f = open('Marks.txt','r')
                    f.readline()
        elif option3 == 7:
            screen.addstr("  Good bye,see you again\n  ")
            screen.refresh()
            curses.napms(1000)
            curses.endwin()
            exit()
        
              
if __name__ == '__main__':
    main()
    
