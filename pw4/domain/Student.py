students = []
studentID = []
studentName = []
studentDoB = []
#----------------------------- Students -----------------------------#
class Student:
    def __init__(self, id, name, DoB):
        self.id = id
        self.name = name
        self.DoB = DoB
        
    def get_id(self):
        return self.id 
    
    def get_name(self):
        return self.name
    
    def get_DoB(self):
        return self.DoB
    
    
    