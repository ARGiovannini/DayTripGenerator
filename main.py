import random
print("")
print("Hola mí amor! I know that we need to go on a real date soon, but for now, lets let this computer program take us on a virtual trip.")
print("")
print("I will just need you to make a few decisions for me.")
print("")
destinations = ["Agribah", "Atlantis", "Beasts castle", "Hawaiian Islands"]
modes_of_transportation = ["Watching a movie", "Reading a book", "Storytime", "Our imagination"]
restaurants = ["A feast for royalty", "Sushi", "Dinner made by teapots", "BBQ"]
entertainment = ["Go on a magic carpet ride", "Go on a seahorse ride", "Dance in the ballroom", "Sail with Maui"]
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
    day_trip_dictionary["destination"] = random_destination

def transportation_picker():
    choice = "N"
    while choice != "Y":
        random_transportation = random.choice(modes_of_transportation)
        choice = input(f"How does {random_transportation} sound for our method of transportation? Please input Y or N: ")
        print("")
    print("Excellent choice!")
    print("")
    day_trip_dictionary["transportation"] = random_transportation

def restaurant_picker():
    choice = "N"
    while choice != "Y":
        random_restaurant = random.choice(restaurants)
        choice = input(f"How does {random_restaurant} sound for our meal? Please input Y or N: ")
        print("")
    print("Excellent choice!")
    print("")
    day_trip_dictionary["restaurant"] = random_restaurant

def entertainment_picker():
    choice = "N"
    while choice != "Y":
        random_entertainment = random.choice(entertainment)
        choice = input(f"How does {random_entertainment} sound for our entertainment? Please input Y or N: ")
        print("")
    print("Excellent choice!")
    print("")
    day_trip_dictionary["entertainment"] = random_entertainment

def run_day_trip_generator():
    destination_picker()
    transportation_picker()
    restaurant_picker()
    entertainment_picker()
    print("Excellent! We will be traveling to " + day_trip_dictionary["destination"])
    print("")
    print("We will travel by way of " + day_trip_dictionary["transportation"])
    print("")
    print("For our meal we will have " + day_trip_dictionary["restaurant"])
    print("")
    print("And for fun we will " + day_trip_dictionary["entertainment"])
    print("")

run_day_trip_generator()
