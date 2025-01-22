with open('sample.txt','r') as file:
    content =file.read()
    print(content)
    """in with there also extra steo for initializelike mode
    def __init(self,filename,mode):\
     self.filename=filename
     self.mode=mode
     self.file=None

try :
  with HandleFile('sample.txt','r') as file:
  content =file.read()
  raise ValueError("Error while reading the file!")

except ValuesError("Error while reading the file!")
  print(e)

print(file.closed)
    """

print(file.closed)
"""python context manager comes role into play 
with statement sets up the context does the work and performs the clean up.
A context manager is a special kind of object in python that knows how to manage resources.
it has two methods __enter__ and __exit__
The enter method handles the setup and exit method takes the care of cleansup 

Class ContextManager:
  def __enter__(self):
   print("Entering context")
   return 'some resource'

  def __exit__(self,ecx_type,exc_value,traceback):
   print("exiting content")

with ContextManager() as cm:
  print(f"Using {cm}")

  interpreter
  when we enter the width block Python calls the enter the method to do the setup gives us access to some resource and when we are done
  or even if something breaks the exit method is called for the cleanup

  
conetext managers are used for various purpose like database connection ,file handling ,Thread locks,and Temporary files and directories
"""