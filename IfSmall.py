#number 1
user = input ("Enter the password\n")

if user == "abc" :
    print ("welcome")
else :
    print ("wrong password try again ")

print ("#############################")
#number 2

user2 = input ("Choose yes, no, maybe\n")

if user2 == "yes" :
    print ("You wrote yes")
elif user2 == "no" :
    print ("You wrote no")
elif user2 == "maybe" :
    print ("You wrote maybe")
else :
    print ("invalid")


print ("############################")
#number 3

user3 = int (input ("Guess the number\n"))

if user3 == 7:
    print ("right guess")
else:
    print ("wrong guess")