from tkinter import *
from tkinter import messagebox

# from module import methods
from output import main_out
from input import main_in
from domain.Student import *
from domain.Course import *
from domain.Mark import *
from compress import Compress
from decompress import Decompress


def main():
    root = Tk()
    root.title('Student Management')
    root.geometry("620x700")
    mainframe = Frame(root)
    mainframe.grid()
    lblmain=Label(mainframe,text='Student Management',font=("Helvetica", 36, "bold"), fg='deep sky blue')
    lblmain.grid(row=0,column=2,padx=100,pady=50)
    
    btn1=Button(text='Enter the number of courses in class',command=main_in.number_course, font=("time", 15, "italic"), fg="RoyalBlue1", width=40)
    btn1.grid(row=2,column=0,padx=5,pady=5)
    
    btn2=Button(text='Add Course in the class',command=main_in.add_course, font=("time", 15, "italic"), fg="RoyalBlue1", width=40)
    btn2.grid(row=3,column=0,padx=5,pady=5)
    
    btn2=Button(text='Enter the number of students in class',command=main_in.number_student, font=("time", 15, "italic"), fg="RoyalBlue1", width=40)
    btn2.grid(row=4,column=0,padx=5,pady=5)
    
    btn3=Button(text='Add Student in the class',command=main_in.add_student, font=("time", 15, "italic"), fg="RoyalBlue1", width=40)
    btn3.grid(row=5,column=0,padx=5,pady=5)
    
    btn4=Button(text='Input Mark',command=main_in.assign_mark, font=("time", 15, "italic"), fg="RoyalBlue1", width=40)
    btn4.grid(row=6,column=0,padx=5,pady=5)
    
    btn7=Button(text='Calculation gpa ',command=main_in.calculation_Gpa, font=("time", 15, "italic"), fg="RoyalBlue1", width=40)
    btn7.grid(row=7,column=0,padx=5,pady=5)
    
    btn5=Button(text='list Courses in the class',command=main_out.display_course, font=("time", 15, "italic"), fg="RoyalBlue1", width=40)
    btn5.grid(row=8,column=0,padx=5,pady=5)
    
    btn6=Button(text='list Student in the class',command=main_out.display_student, font=("time", 15, "italic"), fg="RoyalBlue1", width=40)
    btn6.grid(row=9,column=0,padx=5,pady=5)
    
    btn7=Button(text='list Mark',command=main_out.display_mark, font=("time", 15, "italic"), fg="RoyalBlue1", width=40)
    btn7.grid(row=10,column=0,padx=5,pady=5)
    
    btn8=Button(text='GPA Decending',command=main_out.GPA_decending, font=("time", 15, "italic"), fg="RoyalBlue1", width=40)
    btn8.grid(row=11,column=0,padx=5,pady=5)
    
    btn8=Button(text='Compress',command = Compress, font=("time", 15, "italic"), fg="RoyalBlue1", width=40)
    btn8.grid(row=12,column=0,padx=5,pady=5)
    
    btn9=Button(text='Decompress',command = Decompress, font=("time", 15, "italic"), fg="RoyalBlue1", width=40)
    btn9.grid(row=13,column=0,padx=5,pady=5)

    root.mainloop()
              
if __name__ == '__main__':
    main()
    
