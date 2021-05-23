courses = []
courseID = []
course_Credit = []
courseName = []

#----------------------------- Courses -----------------------------#
class Course:
    def __init__(self, id, name, credit):
        self.id = id
        self.name = name
        self.credit = credit
        
        
    def get_id(self):
        return self.id 
    
    def get_name(self):
        return self.name
    
    def get_credit(self):
        return self.credit        
