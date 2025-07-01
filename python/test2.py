
n1=int(input("Enter a num:"))
if(n1%2==0):
  print(n1,"is even")
else:
  print(n1,"is odd")



M=int(input("Enter total marks out of 500:"))
p=M/5
if(p>85):
    print("Grade A")
elif(p>75):
    print("Grade B")
elif(p>65):
    print("Grade C")
else:
    print("Fail")


age=int(input("Enter age:"))
if(age<18):
    print("not eligble to drive")
else:
    print("eligble to drive")


no1=int(input("Enter num1:"))
n2=int(input("Enter num2:"))
n3=int(input("Enter num3:"))
if(n1>n2 and n1>n3):
    print(no1," is greatest")
elif(n2>n1 and n2>n3):
    print(n2," is greatest")
else:
    print(n3," is greatest")
