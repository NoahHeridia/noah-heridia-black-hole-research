import math #Imports the math library
import random #Imports the random library
import numpy #Imports the numpy library

def Python_basics():
    # Variables and Data Types: 
    x = 5  # int
    y = 2.5  # float
    name = "Alice"  # string
    is_student = True  # bool

    # Basic Input/Output:
    name = input("Enter your name: ") # Overwrites the variable 'name'
    print("Hello, " + name)


    # Simple Math:
    '''
    ----------------------------------------------------------------
    Operatiors:
    +   the addition operator
    -   the subtraction operator
    *   the multiplication operator
    /   the division operator
    **  the exponent operator
    //  the floor division operator (rounds down to the nearest integer)
        # Using x // (10**n) shifts the number right by n places.
            Example: 
            phone_number = 1234567890
            tmp_value = phone_number // 10**4
            # Output: tmp_value = 123456
    %   the modulus operator (gives the remainder from division)
        # Using x % (10**n) get the last n numbers from x
            Example: 
            phone_number = 1234567890
            tmp_val = phone_number % 10**4
            # Output: temp_val = 7890
    ----------------------------------------------------------------
    Compound Operatiors:
    age += 1    age = age + 1
    age -= 1    age = age - 1
    age *= 1    age = age * 1
    age /= 1    age = age / 1
    age %= 1    age = age % 1
    ----------------------------------------------------------------
    
    '''
    
    a = 10
    b = 20
    sum = a + b
    print("First sum: ", sum) # Prints the first sum
    
    c = 15
    sum += c
    print("Second sum: ", sum) # Prints the second sum
    

    
    # Adding sentences
    sentence = name + "'s comments:\n" + input("Write a comment: ")
    print(sentence)
    
################################################################
def Control_flow():
    # If-elif-else statements:
    if x > 0:
        print("x is positive")
    elif x == 0:
        print("x is zero")
    else:
        print("x is non-positive")
    
    # For loops:
    for i in range(5): # range(start, stop, step)
        print(i)
        
    # While loops:
    count = 0
    while count < 3:
        print("Counting: ", count)
        count += 1

################################################################
def Functions():
    # Simple functions
    def greet(name):
        print("Hello, " + name)
    greet("Alice")
    
    def goodbye(name):
        print(f'Goodbye, {name}.')
    goodbye('Dave')
    
    def calc(x):
        y = 4*x + 1
        message = f"y = {y}"
        print(message)
    calc(3.5)
    
################################################################
def Advanced_functions():
    def choice1(x1,x2):
        range_r = ""
        for i in range(int(x1),int(x2)+1):
            range_r += f"{str(i)} "
        return range_r
    
    def choice2():
        a = True
        text = ''
        print('''
              Welcome to the paragraph maker!
              
              Please type words or sentences that you would like to add to a paragraph.
              If you want to exit, type "*exit" without the quotes. 
              This will print your paragraph and bring you back to the main menu.
              ''')
        while a:
            text_in = input("input: ")
            if text_in == "*exit":
                print(f"Output:\n{text}")
                a = False
            else:
                text += text_in

    
    while True:
        choice = input("""
        Hi! Welcome to the main menu.
        
        __________
        What would you like to do today?
        1 - Give me a range from x1 to x2
        2 - Make a paragraph
        3 - End
        """).strip()
        
        try:
            choice = int(choice) # Converts the choice to an integer
        except:
            print("Error: Invalid choice \nPlease enter either '1', '2', '3', or '4' without apostrophes")
        try:
            if choice >= 1 and choice <=3:
                if choice == 1:
                    range_r = choice1(input("Start at: "), input("End at: "))
                    print(range_r)
                if choice == 2:
                    choice2()
                if choice == 3:
                    print("Have a good day!")
                    break
                
            else:
                print("Error: Choice out of range. \nPlease enter either '1', '2', '3', or '4' without apostrophes")
        except:
            print("Error: Invalid choice. \nPlease try again.")




# Assignment:
"""
Simple Calculator Project

Objective:
Create a program that asks the user for two numbers and an operation (addition, subtraction, multiplication, or division) and then outputs the result.

Steps for the Assignment:
(1) Prompt the user for input:
        Two numbers.
        The operation (e.g., +, -, *, /).
(2) Perform the chosen operation:
        Use if-elif-else statements to decide which operation to perform.
(3) Handle division by zero:
        Add a check to ensure the user doesn’t try to divide by zero.
(4) Allow the user to perform multiple calculations:
        Use a while loop to let the user choose to perform another calculation or exit the program.
"""




# Assignment completed:
"""
def calculator():
    while True:
        # Get input from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter an operation (+, -, *, /): ")

        # Perform the operation
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error! Division by zero."
        else:
            result = "Invalid operation."

        print("Result:", result)

        # Ask if they want to do another calculation
        choice = input("Do you want to perform another calculation? (yes/no): ").lower()
        if choice != 'yes':
            break

# Run the calculator
calculator()
"""

#Python_basics()
#Control_flow()
#Functions()
Advanced_functions()
