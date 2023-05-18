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

#----------------For fun!-------------------
def fourth_func(**player): 
    for key, value in player.items():
        print(key + ": " + value.strip(), end=", ")
    print()

fourth_func(first="Jaime", second="Saheed", third="Uche")

#Revised w/o the unnecessary comma at the end
def fifth_func(**player):
    output = []
    for key, value in player.items():
        output.append(key + ": " + value.strip())
    print(", ".join(output))

fifth_func(first="Jaime", second="Saheed", third="Uche")

# Passing a list as an arg
def my_function(food):
#   for x in food:
#     print(x)
#     for i in x:
#        print(i)
    for key, value in food.items():
      print(key, value)

foods = {"fruits": ["apple", "banana", "cherry"],
"vegetables": ["spinach", "onion", "broccoli"]}
my_function(foods)
