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

def print_results(list):
    print('Destination: ' + list[0])
    print('Restaurant: ' + list[1])
    print('Transportation: ' + list[2])
    print('Entertainment: ' + list[3])

def unsatisfied_selection(lists, list_position, list_index, list):
        lists.remove(list_position)
        if lists.__len__() < 1:
            list[list_index] = input('Tell me what you want. Write in your choice. ')
            print_results(list)
            check_satisfaction(list)
        else:
            list[list_index] = random_selector(lists)
            print_results(list)
            check_satisfaction(list)

def check_satisfaction(list):
    answer = input("Are you satisfied with your trip results? Yes or No ")
    while answer == 'no' or answer == 'No' or answer == 'N' or answer == 'n':
        change = input("What would you like to change; A: Destination, B: Restaurant, C: Transportation, or D: Entertainment? ")
        if change == 'Destination' or change == 'destination' or change == 'A' or change == 'a':
            unsatisfied_selection(destinations, list[0], 0, list)
            return list
        
        elif change == 'Restaurant' or change == 'restaurant' or change == 'B' or change == 'b':
            unsatisfied_selection(restaurants, list[1], 1, list)
            return list

        elif change == 'Transportation' or change == 'transportation' or change == 'C' or change == 'c':
            unsatisfied_selection(modes_of_transportation, list[2], 2, list)
            return list

        elif change == 'Entertainment' or change == 'entertainment' or change == 'D' or change == 'd':
            unsatisfied_selection(forms_of_entertainment, list[3], 3, list)
            return list
    while answer == 'yes' or answer == 'Yes' or answer == 'Y' or answer == 'y':
        day_trip_confirmed(list)
        break

def day_trip_confirmed(list):
    print(f"You will be traveling to {list[0]} by {list[2]}, where you will be eating at a {list[1]} and going {list[3]} on your Day Trip! I hope you have a great time!")
        
def day_trip_generator():
    destination = random_selector(destinations)
    restaurant = random_selector(restaurants)
    transportation = random_selector(modes_of_transportation)
    entertainment = random_selector(forms_of_entertainment)
    return [destination, restaurant, transportation, entertainment]

def main():
    print_list = day_trip_generator()
    print_results(print_list)
    check_satisfaction(print_list)
    

main()