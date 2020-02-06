class Person:
    name = "IVAN"
    age = 10

    def __init__(self,age,name):
        self.age = age
        self.name = name
        
    def set(self,age,name):
        self.age = age
        self.name = name

class Student(Person):
    course = 0
    Class = 0
    def Num(self,course,Class,age,name):
        if (age <= 18 and age >= 7):
            s = 18 - age 
            Class = 11 - s
            print(name + " studying in " + str(Class) + " class.")
            return Class
        elif (age >= 18):
            course = 6
            s = 23 - Student.age
            course = course - s
            print(name + " studying in " + str(course) + " course.")
            return course

igor = Student(12,"Igor")
igor.set(15,"Igor")
print(igor.name + " " + str(igor.age))
print(igor.Num(igor.course, igor.Class,igor.age,igor.name))

Greg = Person(13,"Greg")
Greg.set(12,"Greg")
print(Greg.name + " " + str(Greg.age))

Fred = Student(15,"Fred")
print(Fred.name + " " + str(Fred.age))
print(Fred.Num(Fred.course, Fred.Class,Fred.age,Fred.name))
