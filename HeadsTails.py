import random 

print ("Welcome to the Coin Guessing Game!")
input ("Press enter to start...")
print ("""
Choose a method to toss the coin:
1. Using random.random()
2. Using random.randint()
""")

user_choice = int (input ("Enter your choice (1 or 2): "))

if user_choice == 1:
    random_num = random.random()
    if random_num >= .5:
        comp_choice = "heads"
    else:
        comp_choice = "tails"
    user_choice = input ("Enter your guess heads or tails\n").lower()
    if comp_choice == user_choice:
        print ("Congratulations! You won!")
        print (f"The computer's coin toss result was: {comp_choice}")
    else :
        print("sorry, You lost!")
        print (f"The computer's coin toss result was: {comp_choice}")

elif user_choice == 2:
    random_num = random.randint(0,1)
    if random_num == 0 :
        comp_choice = "heads"
    else:
        comp_choice = "tails"
    user_choice = input ("Enter your guess heads or tails\n").lower()
    if comp_choice == user_choice:
        print ("Congratulations! You won!")
        print (f"The computer's coin toss result was: {comp_choice}")
    else :
        print("sorry, You lost!")
        print (f"The computer's coin toss result was: {comp_choice}")
else:
    print ("invalid choice try again.")
       



