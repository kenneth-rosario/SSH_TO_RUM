

class Course:

    def __init__(self, class_code , section ):
        self.class_code = class_code
        self.section = section

    def get_class_code(self):
        return self.class_code

    def get_section(self):
        return self.section
