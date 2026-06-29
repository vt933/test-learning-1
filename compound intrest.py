principal=float(input("enter the principal amount"))

while principal<=0:
    if principal==0:
        print("amount is 0$")
        break
    else:
     principal=float(input("enter the principal amount greater than 0 "))


intrest=float(input("enter the intrest you will get on principal"))

while intrest<=0:
    if intrest==0:
       print(f"the amount you will recieve is {principal:.2f}")
       break
    else:
         intrest=float(input("enter the intrest amount that is greater than zero "))

timeperiod=int(input("enter the timeperiod you have interested in years"))

while timeperiod<=0:
    if timeperiod==0:
        print(f"your final amount is {principal:.2f}")
        break
    else:
     timeperiod=int(input("enter the intrest amount that is greater than zero "))
    
amount=principal*pow(1+intrest/100,timeperiod)

print(f"the final amount after {principal}$investing/depositing for {timeperiod}years is on rate of interest of {intrest} is {amount:.2f}$")



