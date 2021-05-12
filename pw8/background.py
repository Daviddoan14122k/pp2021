import pickle
import threading

class BackgroundThread(threading.Thread):
    def __init__(self, option, data, pickle_dum=None):
        threading.Thread.__init__(self)
        self.__option = option
        self.__data= data
        self.__pickle_dum = pickle_dum

    def run(self):
        if self.__option == "dump":
            if self.__pickle_dum is not None:
                pickle.dump(self.__pickle_dum, self.__data)
            else:
                 return 0
        elif self.__option== "load":
            load_file=pickle.load(self.__data)
            return load_file


def backgroundThreadFunction(option, data, pickle_dum = None):
    backgroundThread=BackgroundThread(option, data ,pickle_dum)
    backgroundThread.start()
    backgroundThread.join()