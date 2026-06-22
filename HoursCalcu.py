user_seconds = input ("please type the number of seconds \n")

seconds_int = int (user_seconds)

hours = seconds_int // 3600
minutes = seconds_int % 3600 // 60
seconds = seconds_int % 3600 % 60 

print("This course is : " + str(hours) + " hours and " 
+ str(minutes) + " minutes and " + str(seconds) + " seconds")

