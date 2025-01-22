"""
decorators are used to add extra feature in a function at compile time
basicaaly in python we can pass a function as argument as python is a functional programming language

"""
def div(a,b):
    print(a/b)

def smart_div(func):

    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner

div=smart_div(div)

div(2,4) 
"""here we  give input a function in smart div and write an inner function logic to swap arguments when conditon is met and return the function
"""