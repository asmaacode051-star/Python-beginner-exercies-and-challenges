owned_books =[]
wish_books = []

# The books you own 
user = input ("Enter the name of a book you own \n")
owned_books.append(user)
user = input ("Enter the name of another book you own (or press Enter to escape)\n")
if user:
    owned_books.append(user)
print (f"Your Library: {owned_books}")

# The books you wish to own 
user = input ("Enter the name of a book you wish want to have in the future\n")
wish_books.append(user)
user = input("Enter the name of a book you wish want to have(or press Enter to escape)\n")
if user:
    wish_books.append(user)
print (f"Your wishlist {wish_books}")

# The books you got from the wishlist
user = input ("Enter the name of a book you got from the wishlist (or press Enter to escape)\n")
if user in wish_books:
    wish_books.remove(user)
    owned_books.append(user)
print (f"Updated library: {owned_books} ")
print (f"Updated wishlist: {wish_books}")

# The books you want to donate
user = input ("Enter the name of a book you wish to donate (or press Enter to escape)\n")
if user in owned_books:
    owned_books.remove(user)

print (f"Final library after donations {owned_books}")

