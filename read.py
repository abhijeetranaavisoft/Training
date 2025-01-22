cou_file=open("C:/Users/Abhijeet/Desktop/training/New Text Document.txt" ,"r")
print(cou_file.readline())
print(cou_file.readable())
print(cou_file.readlines())
for lines in cou_file.readlines() :
    print(lines)


cou_file.close()