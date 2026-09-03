print ("==== Egyption ID Check ====")

nationality = input ("Are you an Egyption ? Type yes or no\n").lower()

if nationality == "yes":
    print ("Good! this first step")
    age = input ("Are you above 18 ? yes or no\n").lower()
    if age == "yes":
        print ("you can have an ID")
    else:
        print ("sorry you can not have an ID")
        print ("Try when you become above 18")
else :
    print ("sorry, you are not Egyptian you can not have an Egyptian ID")

