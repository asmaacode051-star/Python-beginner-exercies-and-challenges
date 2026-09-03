print ("Welcome to our app")

age = int (input ("How old are you?\n"))
license = input ("Do you have a license?\n").lower()

if age > 18 and license == "yes":
    print ("You can drive ")
elif age < 18 or license == "no":
    print ("you can not drive")