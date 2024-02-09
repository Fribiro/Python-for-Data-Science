#a class defines a set of objects and methods
#an object is an instance of a class

class Person:
    gender = "male" #class attribute

    #constructor - initializes a new instance of a class
    def __init__(self,name,age): #__init__ initializes instance attributes
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name}, my age is {self.age}")


person1 = Person("Alice", 25)
print(person1.name)
person2 = Person("Bob", 30)
print(person2.age)

print(person1.say_hello())

class Email:
    def __init__(self,subject,content):
        self.subject = subject #public attribute
        self._content = content #prtected attribute
        self.__read = False #private attribute

    def mark_as_read(self):
        self.__read = True
        return "Email marked as read"
    
    def is_spam(self): #public method
        return "Spam" in self._content
    
#read on namming mangling
    
e = Email("New course","Check this out")
print(e.mark_as_read())

#inheritance
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name,age)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} is studying")

student = Student("John", 20, "QEJNSND")
student.say_hello()
student.study()

#read on encapsulation and polymorphism

class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def drive(self):
        print(f"{self.brand} {self.model} is driving")

    def description(self):
        return f"{self.year} {self.brand}"

car1 = Car("Toyota","Camry",2022)
car2 = Car("Mercedes","G-Wagon",2023)
car1.drive()
print(car2.brand)
car2.description()

class ElectriCar(Car):
    def __init__(self,brand,model,year,battery_capacity):
        super().__init__(brand,model,year)
        self.battery_capacity = battery_capacity

electric_car = ElectriCar("Tesla","Cybertruck",2023,"100 kwh")
print(electric_car.description())

class Vehicle:
    def drive(self):
        pass

class Truck(Vehicle):
    def drive(self):
        return "Truck is driving"
    
def make_drive(vehicle):
    return vehicle.drive()

truck = Truck()
print(make_drive(truck))