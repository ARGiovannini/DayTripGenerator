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
    if random_transportation == "Watching a movie":
        print("I think you chose that one for me ;)")
        print("")
    elif random_transportation == "Reading a book":
        print("Ah! Your favorite.")
        print("")
    elif random_transportation == "Storytime":
        print("We will be enthralled and moved")
        print("")
    elif random_transportation == "Our imagination":
        print("There are no two better at it than you and me.")
        print("")
    day_trip_dictionary["transportation"] = random_transportation

def restaurant_picker():
    choice = "N"
    while choice != "Y":
        random_restaurant = random.choice(restaurants)
        choice = input(f"How does {random_restaurant} sound for our meal? Please input Y or N: ")
        print("")
    if random_restaurant == "A feast for royalty":
        print("Now that sounds fancy! I hope there is a blue genie as our waiter.")
    elif random_restaurant == "Sushi":
        print("YAY! But lets be sure not to eat any of our new friends")
    elif random_restaurant == "Dinner made by teapots":
        print("I just want to see how that works logistically!")
    elif random_restaurant == "BBQ":
        print("That will feel nostalgic!")
        print("")
    print("")
    day_trip_dictionary["restaurant"] = random_restaurant

def entertainment_picker():
    choice = "N"
    while choice != "Y":
        random_entertainment = random.choice(entertainment)
        choice = input(f"How does {random_entertainment} sound for our entertainment? Please input Y or N: ")
        print("")
    if random_entertainment == "Go on a magic carpet ride":
        print("I can show you the wooooooooooorld")
    elif random_entertainment == "Go on a seahorse ride":
        print("Look at this stuff, isn't it neat?")
    elif random_entertainment == "Dance in the ballroom":
        print("beauty and the beaaaaaaaaaast")
    elif random_entertainment == "Sail with Maui":
        print("What can I say except your welcome?!")
    print("")
    day_trip_dictionary["entertainment"] = random_entertainment

def run_day_trip_generator():
    choice = "N"
    while choice != "Y":
        destination_picker()
        transportation_picker()
        restaurant_picker()
        entertainment_picker()
        print(f'Excellent! We will be traveling to {day_trip_dictionary["destination"]} and we will travel by way of {day_trip_dictionary["transportation"]}.')
        print("")
        print(f'For our meal we will have {day_trip_dictionary["restaurant"]}, and for fun we will {day_trip_dictionary["entertainment"]}.')
        print("")
        choice = input("We can generate a new trip if you like. Do you want to keep this one? Please input Y or N: ")
        print("")
    print("")
    print("We are going to have such a wonderful time. Thank you for confirming our date. I look forward to it very much.")
    print("")

run_day_trip_generator()
