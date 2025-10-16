# Created a contact list so anything that has been added or removed will be stored in the dictionary.
contactlist = {

}

# Used while true statement so the input keeps on going.
while True:
    # Created a dictionary for book.
    print()
    print("Contact Book Menu")
    book = {
        "1. Add Contact": 0,
        "2. Delete Contact": 0,
        "3. List Contacts": 0,
        "4. Exit": 0,
    }

    # Used for statement to only print out only the key of the dictionary.
    for x in book:
        print(x)

    # Created an input for the user to choose what they want to do as shown in the dictionary.
    choice1 = input("Enter choice (TYPE THE NUMBER ONLY): ")
    # CHOICE 1:
    # Created an input for the user to enter a name and phone number if they chose 1.
    if choice1 == "1":
        print()
        name = input("Enter the name: ")
        phone = int(input("Enter the phone number: "))
        # Used a while statement so it will keep on going until the user inputs a valid phone number.
            # Made sure that the phone number is 10 digits long.
        while phone < 1000000000 or phone > 9999999999:
            print("Invalid phone number")
            phone = int(input("Enter the phone number: "))
        else:
            print("Contact added successfully!")
        # Contactlist will be stored using this format below once it is successfully added in the contacts.
        contactlist[name] = phone
    # CHOICE 2:
    # Created an input for the user to enter a name if they chose 2.
    elif choice1 == "2":
        print()
        choice3 = input("Enter the name: ")
        # Created a while statement so it will keep on going until the user inputs a valid name that is already in the contact list.
        while choice3 not in contactlist:
            print("Name not found")
            choice3 = input("Enter the name: ")
        else:
            print("Contact deleted successfully!")
            # Once valid, the name that is on the contact list will be deleted. using del function.
            del contactlist[choice3]
    # CHOICE 3:
    # If user goes for 3, they will get a list of all the contacts that are in the contact list.
    # Used a for statement NOT only get the name in the contact list but the number as well
    elif choice1 == "3":
        print()
        for name, phone in contactlist.items():
            print(f"{name}: {phone}")
    # CHOICE 4:
    # Used exit() function to end the program if the user chose 4.
    elif choice1 == "4":
        exit()
    else:
        print("Invalid number")

