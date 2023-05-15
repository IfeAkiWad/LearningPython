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

#Arbitrary Keyword arguments(**kargs)
def third_func(**player):
    print("first place: " + player["first"] + ", second place: " + player["second"] + ", and third place: " + player["third"])

third_func(first = "Jaime", second = "Saheed", third = "Uche")