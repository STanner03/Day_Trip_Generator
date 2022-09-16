import random
# destinations = [input("Tell me 1 place you want to go! "), input("Give me another place you'd like to go. "), input("Give me another place you'd like to go. "), input("Give me another place you'd like to go. "), input("Give me another place you'd like to go. ")]
# restaurants = [input("Tell me a place you want to eat at. "), input("Give me another place you'd like to eat at. "), input("Give me another place you'd like to eat at. "), input("Give me another place you'd like to eat at. "), input("Give me another place you'd like to eat at. ")]
# modes_of_transportation = [input("In what form of transportation do you like to travel? "), input("What is another way you like to travel? "), input("What is another way you like to travel? "), input("What is another way you like to travel? "), input("What is another way you like to travel? ")]
# forms_of_entertainment = [input("What do you like for excitement? "), input("What is something else you want to do? "), input("What is something else you want to do? "), input("What is something else you want to do? "), input("What is something else you want to do? ")]
destinations = ['New York', 'Miami', 'Hawaii', 'Seattle', 'L.A.']
restaurants = ['Texas Roadhouse', 'T.G.I. Fridays', 'Chicken place', 'Taco place', 'Pizza place']
modes_of_transportation = ['Car', 'Motorcycle', 'Air Plane', 'Walking', 'catapult']
forms_of_entertainment = ['Sky Diving', 'Golfing', 'Day Drinking', 'Coding', 'Hiking']

def random_selector(list_to_select_from):
    selection = random.choice(list_to_select_from)
    return selection

def print_results():
    print(print_list)

def check_satisfaction():
    answer = input("Are you satisfied with your trip results? ")
    yes = yes
    no = no
    while answer == no:
        change = input("What would you like to change? Destination, Restaurant, Transportation, Entertainment ")
        if change == destination:
            destination = random_selector(destinations)
    else:
        print(f"Your itenerary for your Day Trip is",{print_list})

def day_trip_generator():

    destination = random_selector(destinations)

    restaurant = random_selector(restaurants)

    transportation = random_selector(modes_of_transportation)

    entertainment = random_selector(forms_of_entertainment)

    return destination, restaurant, transportation, entertainment

print_list = day_trip_generator()
print_results()
check_satisfaction()