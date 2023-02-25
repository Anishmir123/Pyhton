import random

cnumber=random.randrange(1,101)
x=int(input("Enter the number:"))
if x>cnumber:
    print("computer number:",cnumber)
    print("your number is high number")
elif x<cnumber:
    print("computer numberis :",cnumber)
    print("your number is low number")
else :
    print("computer number is:",cnumber)
    print("number is equal")




