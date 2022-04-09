class Student(object):
    def __init__(self, name, grade, iq, school):
        self.name = name
        self.grade = grade
        self.iq = iq
        self.school = school
    
    def start(self):
        print("start")
        return("hello")
    
    def end(self):
        print("end")
        return("goodbye")
student1 = Student("Akash", 5, 100, "Blueberry School")
print(student1.name)
print(student1.end())