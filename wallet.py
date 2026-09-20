import random
print ("Welcome to 'whose wallet?' ")
print ("You will give me a list of names, and I will pick a person")

names = input ("If you are ready, enter the names seperated by a comma\n").split(", ")

person_picked= random.choice (names)    
print (f"Please ask {person_picked} to take his wallet out. Dinner is on him  ")                                                                            