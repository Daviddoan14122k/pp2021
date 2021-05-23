import math
import numpy as np
from domain.Student import *
from domain.Course import *
from domain.Mark import *
from tkinter import *
from tkinter import messagebox


class main_in():
    def number_student():
        root = Tk()
        root.title('Number of students in the Class')
        root.geometry("450x100")

        mainframe = Frame(root)
        mainframe.grid()

        Num_var = StringVar()
        lbl_numStu = Label(mainframe, font=('arial', 15), text="Number Student", padx=10, pady=10)
        lbl_numStu.grid(row=0, column=0)
        txt_numStu = Entry(mainframe, font=('arial', 15), width=22, textvariable=Num_var)
        txt_numStu.grid(row=0, column=1, padx=2)
        
        def number_std():
            try:
                num = int(txt_numStu.get())
                if num <= 0:
                    messagebox.showerror(message="Error: Please enter the number of Student is positive")
                    txt_numStu.delete(0, END)
                else:
                    num = int(txt_numStu.get())
                    root.destroy()
            except:
                messagebox.showerror(message="Invalid number of student")

       
        btnStudent = Button(mainframe,
                        fg="red",
                        font=('arial', 9, 'bold'),
                        text='Take input',
                        command=number_std)

        btnStudent.grid(row=1,column=1,padx=1)

                
                
    # function to enter the number of courses
    def number_course():
        root1 = Tk()
        root1.title('Number of Courses in the Class')
        root1.geometry("450x100")

        mainframe1 = Frame(root1)
        mainframe1.grid()

        Nco_var = StringVar()
        lbl_numCOU = Label(mainframe1, font=('arial', 15), text="Number Courses", padx=10, pady=10)
        lbl_numCOU.grid(row=0, column=0)
        txt_numCOU = Entry(mainframe1, font=('arial', 15), width=22, textvariable=Nco_var)
        txt_numCOU.grid(row=0, column=1, padx=2)
        def NumCOU():
            try:
                Nco = int(txt_numCOU.get())
                if Nco <= 0:
                    messagebox.showerror(message="Error: Please enter the number of Course is positive")
                    txt_numCOU.delete(0, END)
                else:
                      Nco = int(txt_numCOU.get())
                      root1.destroy()
            except:
                messagebox.showerror(message="Invalid number of courses")

        btnCOU = Button(mainframe1,
                        fg="red",
                        font=('arial', 9, 'bold'),
                        text='Take Input',
                        command=NumCOU)

        btnCOU.grid(row=1,column=1,padx=1)
        
    #function to add student
    def add_student():
        student_screen = Tk()
        student_screen.title('Information Student')
        student_screen.geometry("400x170")
        
        mainframe2 = Frame(student_screen)
        mainframe2.grid()
        
        id_var=StringVar()
        lbl_stuId = Label(mainframe2, font=('arial', 10,'bold'), width=22, text="Student Id", padx=10, pady=10)
        lbl_stuId.grid(row=0, column=0)
        txt_stuId = Entry(mainframe2, font=('arial', 10,'bold'), width=22, textvariable=id_var)
        txt_stuId.grid(row=0, column=1, padx=2,sticky="w")
        txt_stuId.focus_set()
        
        name_var=StringVar()
        lbl_stuName = Label(mainframe2, font=('arial', 10,'bold'), width=22, text="Student Name", padx=10, pady=10)
        lbl_stuName.grid(row=1, column=0)
        txt_stuName = Entry(mainframe2, font=('arial', 10,'bold'), width=22, textvariable=name_var)
        txt_stuName.grid(row=1, column=1, padx=2,sticky="w")
        txt_stuName.focus_set()
        
        dob_var=StringVar()
        lbl_studob = Label(mainframe2, font=('arial', 10,'bold'), width=22, text="Date of Bird", padx=10, pady=10)
        lbl_studob.grid(row=2, column=0)
        txt_studob = Entry(mainframe2, font=('arial', 10,'bold'), width=22, textvariable=dob_var)
        txt_studob.grid(row=2, column=1, padx=2,sticky="w")
        txt_studob.focus_set()
        def input_student():
                id=txt_stuId.get()
                name=txt_stuName.get()
                DoB=txt_studob.get()
                
                if id=="":
                    messagebox.showerror(message="Error: Please enter the Student ID")
                elif name=="":
                    messagebox.showerror(message="Error: Please enter the Student Name")
                elif DoB=="":
                    messagebox.showerror(message="Error: Please enter the Student Date of Bird")
                else:
                    s = Student(id,name,DoB)
                    students.append(s)
                    studentID.append(id)
                    studentName.append(name)
                    messagebox.showinfo(message="Successfully added student")
                    student_screen.destroy()
            
        btnStudent = Button(mainframe2,
                        fg="red",
                        font=('arial', 9, 'bold'),
                        text='Take Input',
                        command=input_student)

        btnStudent.grid(row=4,column=1,padx=1)
        
    #function to add course
    def add_course():
        course_screen = Tk()
        course_screen.title('Information course')
        course_screen.geometry("400x170")
        
        mainframe3 = Frame(course_screen)
        mainframe3.grid()
        
        cid_var=StringVar()
        lbl_couId = Label(mainframe3, font=('arial', 10,'bold'), width=22, text="Course ID", padx=10, pady=10)
        lbl_couId.grid(row=0, column=0)
        txt_couId = Entry(mainframe3, font=('arial', 10,'bold'), width=22, textvariable=cid_var)
        txt_couId.grid(row=0, column=1, padx=2,sticky="w")
        txt_couId.focus_set()
        
        name_var=StringVar()
        lbl_couName = Label(mainframe3, font=('arial', 10,'bold'), width=22, text="Course Name", padx=10, pady=10)
        lbl_couName.grid(row=1, column=0)
        txt_couName = Entry(mainframe3, font=('arial', 10,'bold'), width=22, textvariable=name_var)
        txt_couName.grid(row=1, column=1, padx=2,sticky="w")
        txt_couName.focus_set()
        
        credit_var=StringVar()
        lbl_coucredit = Label(mainframe3, font=('arial', 10,'bold'), text="Course Credit", padx=10, pady=10)
        lbl_coucredit.grid(row=2, column=0)
        txt_coucredit = Entry(mainframe3, font=('arial', 10,'bold'), width=22, textvariable=credit_var)
        txt_coucredit.grid(row=2, column=1, padx=2,sticky="w")
        txt_coucredit.focus_set()
        def input_course():
            id=txt_couId.get()
            name=txt_couName.get()
            credit=txt_coucredit.get()
            
            if id=="" :
                messagebox.showerror(message="Error: Please enter Courses ID")
                
            elif name=="":
                messagebox.showerror(message="Error: Please enter Courses Name")
                
            elif credit=="" :
                messagebox.showerror(message="Error: Please enter Courses Credit")
                
            else:
                c = Course(id,name,credit)
                courses.append(c)
                courseID.append(id)
                courseName.append(name)
                course_Credit.append(credit)
                messagebox.showinfo(message="Successfully added Course")
                course_screen.destroy()
            
        btnCoures = Button(mainframe3,
                        fg="red",
                        font=('arial', 9, 'bold'),
                        text='Take Input',
                        command=input_course)

        btnCoures.grid(row=4,column=1,padx=1)


    #function choose corese to assign mark for student
    def assign_mark():
        mark_screen = Tk()
        mark_screen.title('Information mark')
        mark_screen.geometry("400x170")
        
        mainframe4 = Frame(mark_screen)
        mainframe4.grid()
        
        cid_var=StringVar()
        lbl_couId = Label(mainframe4, font=('arial', 10,'bold'), width=22, text="Course Id", padx=10, pady=10)
        lbl_couId.grid(row=0, column=0)
        txt_couId = Entry(mainframe4, font=('arial', 10,'bold'), width=22, textvariable=cid_var)
        txt_couId.grid(row=0, column=1, padx=2,sticky="w")
        txt_couId.focus_set()
        
        id_var=StringVar()
        lbl_stuId = Label(mainframe4, font=('arial', 10,'bold'), width=22, text="Student Id", padx=10, pady=10)
        lbl_stuId.grid(row=1, column=0)
        txt_stuId = Entry(mainframe4, font=('arial', 10,'bold'), width=22, textvariable=id_var)
        txt_stuId.grid(row=1, column=1, padx=2,sticky="w")
        txt_stuId.focus_set()
        
        marks_var=StringVar()
        lbl_marks = Label(mainframe4, font=('arial', 10,'bold'), width=22, text="Mark", padx=10, pady=10)
        lbl_marks.grid(row=2, column=0)
        txt_marks = Entry(mainframe4, font=('arial', 10,'bold'), width=22, textvariable=marks_var)
        txt_marks.grid(row=2, column=1, padx=2,sticky="w")
        txt_marks.focus_set()
        def input_mark():
            c_id=txt_couId.get()
            if (c_id=="") or (c_id  not in courseID):
                    messagebox.showerror(message="Error: Please enter the Course ID")
            elif c_id in courseID:
                s_id=txt_stuId.get()
                if (s_id=="") or (s_id  not in studentID):
                    messagebox.showerror(message="Error: Please enter the Student ID")
                elif s_id in studentID:
                    score=float(txt_marks.get())
                    if score<0 or score >20:
                        messagebox.showerror(message="Error: Please enter the mark in range(0,20)")
                    else:
                        score=float(txt_marks.get())
                        mark = math.floor(score)
                        m = Mark(s_id,c_id,mark)
                        mark_detail.append(mark)
                        marks.append(m)
                        mark_screen.destroy()
        btnMark = Button(mainframe4,
                        fg="red",
                        font=('arial', 9, 'bold'),
                        text='Take input',
                        command=input_mark)

        btnMark.grid(row=4,column=1,padx=1)
        
    # function to assign gpa in mark list
    def calculation_Gpa():     
        GPA_screen = Tk()
        GPA_screen.title('Information Gpa')
        GPA_screen.geometry("400x150")
        
        mainframe5 = Frame(GPA_screen)
        mainframe5.grid()
        value=np.array([mark_detail])
        cre=np.array([course_Credit])
        
        id_var=StringVar()
        lbl_stuId = Label(mainframe5, font=('arial', 10,'bold'), width=22, text="Student Id", padx=10, pady=10)
        lbl_stuId.grid(row=0, column=0)
        txt_stuId = Entry(mainframe5, font=('arial', 10,'bold'), width=22, textvariable=id_var)
        txt_stuId.grid(row=0, column=1, padx=2,sticky="w")
        txt_stuId.focus_set()
        def cal():
            id=txt_stuId.get()
            if (id=="") or (id  not in studentID):
                messagebox.showerror(message="Error: Please enter the Student ID")
                
            elif id in studentID:
                for i in range(0,len(marks)):
                    totalCredit=np.sum(cre)
                    totalValue=np.sum(np.multiply(value,cre))
                    i = i + 1
                gpa=totalValue/totalCredit
            else: 
                messagebox.showerror(message="Error: Please enter the Course ID")
            mark_gpa.append(gpa)
            GPA_screen.destroy()

        btnGPA= Button(mainframe5,
                        fg="red",
                        font=('arial', 9, 'bold'),
                        text='Calculate_GPA',
                        command=cal)

        btnGPA.grid(row=1,column=1,padx=1)
        