import pickle
from domain.Student import *
from domain.Course import *
from domain.Mark import *
from background import BackgroundThread
from background import backgroundThreadFunction

def Compress():
    with open('Student.dat', 'wb') as file_students:
        backgroundThreadFunction(option="dump", data = file_students, pickle_dum=len(students))
        for st in students:
            backgroundThreadFunction(option="dump", data = file_students, pickle_dum = st)

        backgroundThreadFunction(option="dump", data = file_students, pickle_dum=len(courses))
        for cs in courses:
            backgroundThreadFunction(option="dump", data = file_students, pickle_dum = cs)

        backgroundThreadFunction(option="dump", data = file_students, pickle_dum=len(marks))
        for ms in marks:
            backgroundThreadFunction(option="dump", data = file_students, pickle_dum = ms)
    file_students.close()