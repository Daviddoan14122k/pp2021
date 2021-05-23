import os
import pickle
from domain.Student import *
from domain.Course import *
from domain.Mark import *
from background import BackgroundThread
from background import backgroundThreadFunction

def Decompress():
    if os.path.isfile('students.dat'):
        # open file, where you stored the pickled data
        file_open = open('students.dat', 'rb')
        database = open('student.txt', 'wb')

        #  dump information to that file
        student_data = backgroundThreadFunction(option="load", data = file_open)
        backgroundThreadFunction(option="dump", data = database, pickle_dum = student_data)

        # close the file
        database.close()
        file_open.close()