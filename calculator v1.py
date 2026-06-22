x=int(input("enter first no:-"))
y=int(input("enter second no:-"))
opertator=input("enter + or add - or minus divide or / mutiply or *:-")
if opertator=="+" or  opertator=="addition":
    print(x+y)
elif opertator=="-" or   opertator=="minus":
    print (x-y)
elif opertator=="*" or  opertator=="multiply":
    print (x*y)
elif opertator=="/"or  opertator=="divide":
 print(x/y)
else:
  print("invalid operator")
