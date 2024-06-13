#
class Student:
    def __init__(self, first_name, last_name, email, course_id):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.course_id = course_id

    def get_student_id(self):
        return self.id
    
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    
    def get_email(self):
        return self.email
    
    def get_course_id(self):
        return self.course_id
    
    def set_course_id(self, course_id):
        self.course_id = course_id
