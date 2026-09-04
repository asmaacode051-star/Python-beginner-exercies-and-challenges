import random 

comp_num = random.randint(1000,9999)
user_num = int (input ("Enter a 4-digits PIN code:\n"))

if len (str(user_num)) != 4 :
    print ("please enter 4 digits ")
elif comp_num == user_num :
    print ("Good guess!")
else:
    print ("Faliur! PIN code did not match.")
    print (f"The computer generated this PIN: {comp_num}")