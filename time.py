#a variable that allows to enter timeperiod by taking userinput
my_time=int(input("enter the timeperiod"))
#time is a module that let's us introduce a lot of time related variables
import time
 #sleep function is a function which suspends any code actitvy till its defined timeperiod.similar to a timer
#this for loop will start from 0 and ends one second before my_time.
#for loop will first see the range x element that is the current element then print it then sleep for one second that for each second it will stop for one second like when x goes from 1 to 2 it will be like 1 and then one second later two.the -1 count backwards whereas -2 count backwards etc.etc
for x in range(my_time,0,-1):
#for seconds in the project we divide x that is also a value in second and module it by 60 as when we divide it by 60 assume that total time in second is 62 so when 62/60 remainder is 2 hence 2 second remain in terms of second for now if timer comes down to 61 we do the same 61/60 is 1 so one second remains in terms of time when the same happens for 60/60 remainder is 0 so no time remains when 59 second remain 59/60 and remainder is 59 and this process continue till programme reach 0 sec
 seconds=int(x%60)
#minutes are not as easy as seconds to run this programme in term of minutes we divide x/60 and then module it by 60 you may ask why so lets deep dive into if put user input as 65 second the 65/60 will be be greater than 1 till it reaches 60 second here when it reaches 60 sec 60/60 becomes 1 and its remainder is also one so time is 1:00 but after it will be less then 1 hence the module is 0 so we will see time in terms of min as zero for any value in second less than 60.
 minutes=int(x/60)%60
#for hours if not including day its much simpler as hours has basic rule if seconds are greater than 3600 or equal to 3600 it is either 1 or greater than it as we can see let us assume that we have 7230 second rundown so till it does not reach 7200 x will be slighly greater than 2 that is approximately 2.something whereas when it reaches 7200 7200/3600 is exactly 2 that is 2  hours and similarly it keeps working till x>3600 when x<3600 assume 3599 3599/3600 is less than 1 somewhere near 0 so it will show less than one ouput will be always==0 approximately and four hours we only care about one variable i.e. hour
 hours=int(x/3600)
 print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
 time.sleep(1)
#just works like range function for given value and does not print anything till the given value.

