

"""
class Myclass :
    x=5

p1=Myclass()
print(p1.x)

__init__ Method:

The __init__ method is a special method in Python that acts as the constructor for a class.
It is called automatically when you create an object of the class.
"""
class Person:
    def __init__(self, name, age):
     self.name= name 
     self.age = age

name= input('Enter your name: ')
age=input('Enter your age : ')

p1 = Person( name, age)
print(p1.age)
print(p1.name)
# we can delete object using del p1 or del p1.age
# we can use class without having values and we can continue coding
# class Person:
#       pass     donot giving any error 

