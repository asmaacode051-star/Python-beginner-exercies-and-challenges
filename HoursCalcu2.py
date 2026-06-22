user = int (input ("Please enter the number of seconds : \n"))
hours = user // 3600
minutes = user % 3600 // 60
seconds = user % 3600 % 60
print(f"The course is : {hours} hours and {minutes} minutes and {seconds} seconds")