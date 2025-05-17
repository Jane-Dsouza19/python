<<<<<<< HEAD

def greet():
    print("Hello! Welcome to the program")
greet() 

def greet_user (name):
    print ("Hello " + name + "! Welcome to the program")
greet_user("John")

def greet_user():
    name = input("Please enter your name: ")  # Prompt the user to enter their name
    print("Hello " + name + "! Welcome to the program")

greet_user()

a= float(input("Enter a value: "))
b= float(input("Enter a value: "))
def add(a, b):
    return a + b    
result = add (a, b)
print("The sum of the two numbers is: " ,result)


def Fahrenheit_to_Celsius():
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    return celsius
print("Temperature in Celsius is: ", Fahrenheit_to_Celsius())

def Celsius_to_Fahrenheit():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
print("Temperature in Fahrenheit is: ", Celsius_to_Fahrenheit())

def display_menu():
    print("\nMenu:")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    print("3. Exit")

while True:  # Start an infinite loop
    display_menu()  # Show the menu
    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
        print("Temperature in Celsius is:", Fahrenheit_to_Celsius())
    elif choice == "2":
        print("Temperature in Fahrenheit is:", Celsius_to_Fahrenheit())
    elif choice == "3":
        print("Goodbye!")
        break  # Exit the loop if the user chooses "3"
    else:
        print("Invalid choice, please enter 1, 2 or 3.")
=======

def greet():
    print("Hello! Welcome to the program")
greet() 

def greet_user (name):
    print ("Hello " + name + "! Welcome to the program")
greet_user("John")

def greet_user():
    name = input("Please enter your name: ")  # Prompt the user to enter their name
    print("Hello " + name + "! Welcome to the program")

greet_user()

a= float(input("Enter a value: "))
b= float(input("Enter a value: "))
def add(a, b):
    return a + b    
result = add (a, b)
print("The sum of the two numbers is: " ,result)


def Fahrenheit_to_Celsius():
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    return celsius
print("Temperature in Celsius is: ", Fahrenheit_to_Celsius())

def Celsius_to_Fahrenheit():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
print("Temperature in Fahrenheit is: ", Celsius_to_Fahrenheit())

def display_menu():
    print("\nMenu:")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    print("3. Exit")

while True:  # Start an infinite loop
    display_menu()  # Show the menu
    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
        print("Temperature in Celsius is:", Fahrenheit_to_Celsius())
    elif choice == "2":
        print("Temperature in Fahrenheit is:", Celsius_to_Fahrenheit())
    elif choice == "3":
        print("Goodbye!")
        break  # Exit the loop if the user chooses "3"
    else:
        print("Invalid choice, please enter 1, 2 or 3.").

>>>>>>> 67d688c (Initial commit: added main.py)
