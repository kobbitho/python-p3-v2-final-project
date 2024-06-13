#
class Course:
    def __init__(self,course_name, course_code, course_description):
        self.course_name = course_name
        self.course_code = course_code
        self.course_description = course_description

    def get_course_id(self):
        return self.id
    
    def get_course_name(self):
        return self.course_name
    
    def get_course_code(self):
        return self.course_code
    
    def get_course_description(self):
        return self.course_description