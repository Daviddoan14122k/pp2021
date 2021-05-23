import numpy as np
from domain.Student import *
from domain.Course import *
from domain.Mark import *
from tkinter import *
from tkinter import messagebox


class main_out():
    #function to display students
    def display_course():
        root = Tk()
        root.title('Coures')
        root.geometry("400x200")
        
        mainframe = Frame(root)
        mainframe.grid()
        
        lbl1=Label(mainframe,text="List Courses in the Class")
        lbl1.grid(row=0,column=0)
        for cor in courses:
            lblcourse=Label(mainframe,text=" [cid: ] %s  [Name: ] %s   [credit: ] %s \n" % (cor.get_id(), cor.get_name(), cor.get_credit()))
            lblcourse.grid(row=(courses.index(cor) + 1), column=0)

    #function to display courses
    def display_student():
        root1 = Tk()
        root1.title('Student')
        root1.geometry("400x200")
        
        mainframe1 = Frame(root1)
        mainframe1.grid()
        
        lbl2=Label(mainframe1,text="List Students in the Class")
        lbl2.grid(row=0,column=0)
        for stu in students:
            lblstudents=Label(mainframe1,text=" [id: ] %s  [Name:] %s   [DoB:] %s \n" % (stu.get_id(), stu.get_name(), stu.get_DoB()))
            lblstudents.grid(row=(students.index(stu) + 1), column=0)
        
    #function to display mark of student given the course
    def display_mark():
        root2= Tk()
        root2.title('Mark')
        root2.geometry("500x200")
        
        mainframe2 = Frame(root2)
        mainframe2.grid()
        
        lbl3=Label(mainframe2,text="Mark list")
        lbl3.grid(row=0,column=0)
        for m in marks:
            lblstudents=Label(mainframe2,text=" [Mark_coursesid: ] %s  [Mark_studentid: ] %s   [Mark_mark: ] %s \n" % (m.get_cid(), m.get_sid(), m.get_mark()))
            lblstudents.grid(row=(marks.index(m) + 1), column=0)
            
    #function to sort GPA decending
    def GPA_decending():
        root3= Tk()
        root3.title('GPA')
        root3.geometry("400x200")
        
        mainframe3 = Frame(root3)
        mainframe3.grid()
        
        lbl3=Label(mainframe3,text="GPA decending")
        lbl3.grid(row=0,column=0)
        
        arr=np.array([mark_gpa])  
        arr[::-1].sort()
        lbl4=Label(mainframe3,text="The list after sorting is %s: \n" %(arr))
        lbl4.grid(row=0,column=0)
