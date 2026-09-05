color_list =[]
user_fav = input ("Add the first color you like\n")
color_list.append(user_fav)

user_choice = input ("Do you want to add more colors? Yes or no\n").lower()

if user_choice == "yes":
    user_fav = input ("Add another color to the list\n")
    color_list.append(user_fav)
    print(f"Your favorite color list is {color_list}")
else:
    print(f"Your favorite color list is {color_list}")
