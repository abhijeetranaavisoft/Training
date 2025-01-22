""" generator is used to fetech the iterator by using yield function which is a generator practical uses is that we can get any partiular data when are millions of data 
in a database   """
def topten():

    yield 1
    yield 2
    yield 3
    yield 4

values=topten()

print(values.__next__())
print(values.__next__())

for i in values:
    print(i)