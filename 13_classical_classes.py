"""
Task 1: People Class
Define a class called Person with attributes name and age.
Then, write a method within the class to introduce the person with their name and age.

Create a new object using this new class, and call the method you created.
"""

print()
print("TASK 1: ")
class Person:
    def __init__(self, name, age):
        # saved the variables name and age to the class
        self.name = name
        self.age = age


    def intro(self):
        # Created another function that loads the other function in the class.
        print(f"Hello I am {self.name} and I am {self.age} years old")
    
# Gave an input by creating a new variable for the class
Kael = Person("Kael", 17)

# Prints out the function that has the given result.
Kael.intro()



"""
Task 2: Animals Speak
Create a base class Animal with a empty method called speak. 

Then create two subclasses, Dog and Cat, each with their own speak method. 

Create objects using these subclasses and call the speak method.
"""

print()
print("TASK 2:")
class Animal:
    pass # Passes down to the subclasses of dog and cat thats inside the Animal class

class Dog(Animal):
    def speak(self):
        # printed Bark! because this is a dog
        print("Bark!")
class Cat(Animal):
    def speak(self):
        # printed meow because this is a cat
        print("Cat: Meow!")


# Two variables = classes so it prints out on what they will speak.
dog = Dog()
cat = Cat()

dog.speak()
cat.speak()
    

"""
Task 3: Banking
Create a class BankAccount with attributes balance and owner. 

Include methods for depositing and withdrawing money, which should modify the balance attribute.

Test these methods with instances of the class.
"""

print()
print("TASK 3: ")

class BankAccount():
    def __init__(self, owner):
        # Saved the variable names for managing money and displaying name
        self.balance = 0
        self.owner = ""
    
    def deposit(self, amount):
        if amount > 0:
            print("Success!")
        else:
            print("Error")
    
    def withdraw(self, amount):
        if amount > 0:
            print("Success!")
        else:
            print("Error.")
    