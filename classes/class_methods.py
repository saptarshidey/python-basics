# define class
class Student:
    def __init__(self, name, age, cgpa):
        self.name = name
        self.age = age
        self.cgpa = cgpa

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_cgpa(self):
        return self.cgpa

class Course:
    enrolled_students = 0

    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            Course.increase_count()

    def get_students(self):
        return len(self.students)

    '''@classmethod
    def increase_count(cls):
        cls.enrolled_students += 1'''

    @staticmethod
    def increase_count():
        Course.enrolled_students += 1

    @staticmethod
    def get_all_students():
        return Course.enrolled_students

# create objects
mark = Student('Mark', 18, 8.7)
ana = Student('Ana', 20, 7.7)

print(f"{mark.get_name()} {mark.get_age()} {mark.get_cgpa()}")
print(f"{ana.get_name()} {ana.get_age()} {ana.get_cgpa()}")

maths = Course('Maths', 1)
maths.add_student(mark)
maths.add_student(ana)
print(maths.get_students())

arts = Course('Arts', 1)
arts.add_student(mark)
arts.add_student(ana)
print(arts.get_students())

print(Course.get_all_students())
