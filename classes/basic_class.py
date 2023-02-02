# define class
class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_major(self):
        return self.major

# create objects
mark = Student('Mark', 18, 'CS-101')
ana = Student('Ana', 20, 'EN-540')

print(f"{mark.get_name()} {mark.get_age()} {mark.get_major()}")
print(f"{ana.get_name()} {ana.get_age()} {ana.get_major()}")
