"""handling errors while intereptting or errors while running the program  are both done using exceptions """

"""for code refer to better python channel github there a lot of exception handling types in python and different is superclass or subclass python exception class

low level database operational  error highlevel error like notfounderror and notauthorized error method like raise and abort are used here

"""
""" another method we can use in for handling errors in python using context manager """
"""
In Python, the self method (technically, the self parameter) is a convention used in object-oriented programming to refer to the instance of the class that is being worked on. Let’s break it down:

1. What Is self?
self is the first parameter of any instance method in a class.

It refers to the current object (or instance) of the class through which the method is being called.
Using self, you can access the instance's attributes and other methods within the class.

2. Why Use self?

Python classes are blueprints for creating objects, and self represents the specific object (instance) that is interacting with the method or attribute.
It allows you to differentiate between instance variables (specific to each object) and class variables (shared across all objects).

3. How self Works:

When you define a method in a class, the first parameter must be self to access the instance.
When calling the method, Python automatically passes the instance as the first argument.


except Exception as e:
"""
import sqlite3

class SQLite:
    def __init__(self,file="application.db"):
        self.file=file

    def __enter__(self):
        self.conn=sqlite3.connect(self.file)
        return self.conn.cursor()
    def __exit__(self,type,value,traceback):
        self.conn.close()
 


   
   
"""
 refer to arjancodes
sometimes there is some connection error or some connection loss pascket error if we try again and again then it maybe work there is a nice function that i found that models this
behaviour that is retry function
def retry(ExceptionTpCheck,tries=4,delay=3,backoff=3,logger=None):
basically it is a complex function which created a decorator that we can wrap around a function that keeps track of number of tries ,puts a delay between them and if 
there is a exception it waits a bit then tries it again for number of times
retry decorator
@retry(Exception,tries=4)
def test_fail(text):
  raise Exception("fail")

test_fail("it works")


we can also log the error
@exception(logger):
def divideByZero():
return 12/0

#Driver code

if __name__=='__main__':
   divideByZero()

   the first problem with exception that they introduce a second hidden control
   flow in your prpgram and second problem is that it results
   in resource leaks in case of an error not closing database connection
   the third  problem exception may introduce extra couling 
   high level system may need to know about low level exception objects if you
   donot set it up right
   its also not what error values are
   solution are
   return dummy but legal value fromn functions but a global error like global error stack lots of coupling
   other method return a legal value but also set on error flag as a funciton result
   return a error code or call exception handler but fall in call back hell                                        

"""