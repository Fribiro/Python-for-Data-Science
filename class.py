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
    
e = Email("Check this out")
print(e.mark_as_read())