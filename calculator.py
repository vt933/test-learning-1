#calculator.py

menu_funtion=("1.addition",
              "2.Subtraction",
              "3.Multiplication",
              "4.Division",
              "5.exit",
)

def addition(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def division(a,b):
    if b==0:
       return("number is not divisble by zero")
    else:
       return a/b

def multiplication(a,b):
    return a*b
while True:
 for item in menu_funtion:
  print(item)
 user_input=int(input("enter user input as(1,2,3,4,or5)"))
 if user_input==5:
    break
 a=float(input("enter the number you want to perform operation on"))
 b=float(input("enter the number you want to perform operation on"))
 if user_input==1:
    result=addition(a,b)
    print(result)

 elif user_input==2:
    r2=subtraction(a,b)
    print(r2)
 elif user_input==3:
    r3=multiplication(a,b)
    print(r3)

 elif user_input==4:
    r4=division(a,b)
    print(r4)
 else:
    print(f"invalid input {user_input}") #happy now dance to full extent as i have added a and b variables