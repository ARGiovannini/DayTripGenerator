import random
print("")
print("Hola mí amor! I know that we need to go on a real date soon, but for now, lets let this computer program take us on a virtual trip.")
print("")
print("I will just need you to make a few decisions for me.")
print("")
destinations = ["Agribah", "Atlantis", "Beasts castle", "Hawaiian Islands"]
modes_of_transportation = ["Movie", "Book", "Storytime", "Imagination"]
restaurants = ["A feast for royalty", "Sushi", "Dinner made by teapots", "BBQ"]
entertainment = ["Magic carpet ride", "Seahorse ride", "Dancing in the ballroom", "Sailing with Maui"]
day_trip_dictionary = {}
def destination_picker():
    choice = "N"
    while choice != "Y":
        random_destination = random.choice(destinations)
        choice = input(f"How does {random_destination} sound for our destination? Please input Y or N: ")
        print("")
    if random_destination == "Agribah":
        print("Perfect! I can't wait to see the architecture of such gorgeous buildings in person.")
        print("")
    elif random_destination == "Atlantis":
        print("I knew you would like that destination. Lets get our fins ready for an amazing underwater adventure.")
        print("")
    elif random_destination == "Beasts castle":
        print("Get your nicest dress, but be sure that you wear shoes comfortable enought to dance in.")
        print("")
    elif random_destination == "Hawaiian Islands":
        print("The water will be so nice! I wonder if we will have to fight a volcano!")
        print("")
    

def transportation_picker():
    choice = "N"
    while choice != "Y":
        random_transportation = random.choice(modes_of_transportation)
        choice = input(f"How does {random_transportation} sound for our method of transportation? Please input Y or N: ")
        print("")
    print("Excellent choice!")        

def restaurant_picker():
    choice = "N"
    while choice != "Y":
        random_restaurant = random.choice(restaurants)
        choice = input(f"How does {random_restaurant} sound for our meal? Please input Y or N: ")
        print("")
    print("Excellent choice!")        

def entertainment_picker():
    choice = "N"
    while choice != "Y":
        random_entertainment = random.choice(entertainment)
        choice = input(f"How does {random_entertainment} sound for our entertainment? Please input Y or N: ")
        print("")
    print("Excellent choice!")

def run_day_trip_generator():
    destination_picker()
    transportation_picker()
    restaurant_picker()
    entertainment_picker()

run_day_trip_generator()
