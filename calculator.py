from My_def import *
import os

print("Welcome to myCalculator!")
name= input("Enter Name?")
begin = input("Would You Like To Begin ? " + name +"(Y/N)")
if begin == ("Y") or ("y"):
   print(" ")
else:
    print("Thanks For Trying My Quiz!!")
X= int(input("Enter First num: ")) 
func=input("Pls enter a option +, - , * , / :") 
Y= int(input("Enter Second Number: "))
if func=="+":
    ans=add(X,Y)
    print(ans)
else:
    pass

if func=="+":
    ans=add(X,Y)
    print(ans)
else:
    pass

if func=="-":
    ans=sub(X,Y)
    print(ans)
else:
    pass

if func=="*":
    ans=mult(X,Y)
    print(ans)
else:
    pass

if func=="/":
    ans=div(X,Y)
    print(ans)
else:
  pass
