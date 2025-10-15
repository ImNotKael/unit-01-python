contactlist = {

}

print()
while True:
    book = {
        "1. Add Contact": 0,
        "2. Delete Contact": 0,
        "3. List Contacts": 0,
        "4. Exit": 0,
    }


    for x in book:
        print(x)
    
    choice1 = input("Enter choice")
    if choice1 == "1":
        print()
        name = input("Enter the name ")
        phone = input("Enter the phone number ")
        contactlist[name] = phone
    elif choice1 == "2":
        choice3 = input("Enter Name: ")
    elif choice1 == "3":
        for x in contactlist:
            print(x)
    elif choice1 == "4":
        choice2 = input("Enter Name: ")
    else:
        print("Invalid number")

