marks = []
mark_detail = []
mark_gpa = []

#----------------------------- Marks -----------------------------#
class Mark:
    def __init__(self, s_id, c_id, mark, gpa=0):
        self.s_id = s_id
        self.c_id = c_id
        self.mark = mark
        self.gpa = gpa
      
    
    def get_cid(self):
        return self.c_id 
    
    def get_sid(self):
        return self.s_id
    
    def get_mark(self):
        return self.mark
    
    def get_gpa(self):
        return self.gpa
    
    def set_gpa(self, gpa):
        self.gpa = gpa
    
    