# Defining a Function
def a_function():
    print("I just defined a function!")

# Calling a function
a_function()

# Function arguments
def another_function(fruit):
    print("I love " + fruit)

another_function("oranges")

# Arbitrary functions (*args)
def third_function(*kids):
    print("The youngest is " + kids[-1])

third_function("Ife", "Toyin", "Toyo", "Tito")
