basket_list = [["Apples","Bananas"],["Milk","Water"]]
print (basket_list)

basket_list[0].insert(0,"Oranges")
basket_list[0].append("Kiwis")
basket_list[1].remove("Water")
basket_list[1].insert(0,"Coffee")
basket_list[1].append("Tea")
basket_list.append([1,2,3])

input("Press enter to change the content...")
print (f"Here is the updated basket\n{basket_list}")