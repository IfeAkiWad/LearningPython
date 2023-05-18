class Pastry:
    def __init__(self, name, type, ingredients, cookTime):
        self.name = name
        self.type = type
        self.ingredients = ingredients
        self.cookTime = cookTime

    def Oven(self):
        print("mm mm! Smells great!")

class Croissant(Pastry):
    pass

class Baklava(Pastry):
    def Oven(self):
        print ("Needs more time!")

class Cannoli(Pastry):
    pass

pastryOne = Croissant("The Croissant", "Filo pastry", {"Ingredients": ["Flour", "sugar", "butter", "eggs", "wine", "cinnamon", "ricotta cheese", "powdered sugar"]}, "10-15 minutes")
pastryTwo = Baklava("The Baklava", "Filo pastry", {"Ingredients": ["Flour", "sugar", "butter", "eggs", "wine", "cinnamon", "ricotta cheese", "powdered sugar"]}, "10-15 minutes")
pastryThree = Cannoli("The Cannoli", "Filo pastry", {"Ingredients": ["Flour", "sugar", "butter", "eggs", "wine", "cinnamon", "ricotta cheese", "powdered sugar"]}, "10-15 minutes")

for x in (pastryOne, pastryTwo, pastryThree):
    print(x.name)
    print(x.type)
    print(x.ingredients)
    print(x.cookTime)
    x.Oven()