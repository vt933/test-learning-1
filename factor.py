
#takes input number to be factored
number_to_factor=int(input("enter the number you would like to factor"))
#we take i as an element of range 2,number_to_factor here when i is in that range 

for i in range(2,number_to_factor):
#we take variable x as number_to factor module and think when we divide a factor by itself there is no remaninder that is the key idea here

    x=number_to_factor%i
#so when x is completely divided by an factor that is it leaves no remainder 

    if x==0:
    #so when this condition is true we print i that are true conditons when we leave no remainder
    #1 is not in range as one is always a factor of each number so no need to keep it in range always write it as a factor
    #number to factored is not included in range as range does not include its ending element untill and unless its done however a number is always a factor of itself so we add it in factors aswell

        print(i,number_to_factor,1)        


        
