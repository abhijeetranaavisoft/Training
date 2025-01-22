from contextlib import contextmanager
"""
The @contextmanager decorator is used to turn a generator function into a context manager.
 The function open_file is decorated with it.
The @contextmanager decorator (from Python's contextlib module) is a tool that simplifies the process of creating a custom context manager.

Without @contextmanager, you would typically need to write a full class with __enter__ and __exit__ methods to define a context manager.

Instead, you can use @contextmanager to turn a simple generator function into a fully functional context manager.

When you use the @contextmanager decorator, it processes a generator function to control the flow of the with statement:

Before the yield statement: The setup code is executed (e.g., opening a file).

At the yield statement: The resource is provided to the caller (e.g., the file object).

After the yield statement: The cleanup code is executed (e.g., closing the file),




 regardless of whether the code inside the with block ran successfully or raised an exception.

"""
@contextmanager
def open_file(file,mode):
    try:
        f=open(file,mode)
        yield f
    finally:
        f.close()

with open_file('sample.txt','w') as f:
    f.write('Lorem ipsum dolor as sut jkdsjka hjsab au')

print(f.closed)