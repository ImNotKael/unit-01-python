# Created a list so anything can be added
my_list = []

print()
print("You have nothing on your list!")
print()
# Made sure to use while TRUE so the input gets to keep on asking whether if the user will add or remove something
while True:
    addedlist = input("Would you like to add or remove inside your list? ")
    if addedlist == "add":
        my_list.append(input("What would you like to add? "))
    elif addedlist == "remove":
        index = int(input("What number would you like to remove? (TOP TO BOTTOM)" ))
        del my_list[index-1]
    else:
        print("Invalid")
        print() 
    print()
    for x in my_list:
        print(x)
    print()




