nums=[1,24,5,6]

"""
for i in nums:
   print(i)
"""

it=iter(nums)

print(it.__next__())
print(it.__next__())
print(it.__next__())
""" same as above print(next(it))"""

class TopTen:

    def __init__(self):
        self.num=1

    def __iter__(self):
        return self
    
    def __next__(self):

        if self.num <=10:
            val=self.num
            self.num +=1

            return val
        else:
            raise StopIteration
        
values=TopTen()
print(next(values))
