user = input ("Choose the area : (Cairo), (Tanta), (Alexandria)\n").lower()

if user == "cairo":
    print ("you chose Cairo")
elif user == "tanta" :
    print ("Tanta is Nice!")
elif user == "alexandria" :
    print ("sounds like a summer")
else :
    print (f"sorry, {user} is not in our list")