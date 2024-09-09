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
    for i in range(5):
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
    while True:
        choice = input.strip("""
        Hi! Welcome to the main menu.
        
        __________
        What would you like to do today?
        1 - Give me a range
        2 - Give me a range with an excluded range
        3 - Make a paragraph
        4 - End
        """)
        
        try:
            choice = int(choice) # Converts the choice to an integer
        except:
            print("Error: Invalid choice \nPlease enter either '1', '2', '3', or '4' without apostrophes")
        
        if choice >= 1 and choice <=4:
            if choice == 1:
                bla
            if choice == 2:
                bla
            if xhoice == 3
        else:
            print("Error: Choice out of range. \nPlease enter either '1', '2', '3', or '4' without apostrophes")
        
        
    
    
        
    
    
