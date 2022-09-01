#Rewrite Exercise 11.40 using a dictionary to store the pairs of states and capitals so that the questions are randomly displayed.
import random


def main(): 

    statedict = {
        'Alabama': 'Montgomery',
        'Alaska': 'Juneau',
        'Arizona': 'Phoenix',
        'Arkansas': 'Little Rock',
        'California': 'Sacramento',
        'Colorado': 'Denver',
        'Connecticut': 'Hartford',
        'Delaware': 'Dover',
        'Florida': 'Tallahasse',
        'Georgia': 'Atlanta',
        'Hawaii': 'Honolulu',
        'Idaho': 'Boise',
        'Illinois': 'Springfield',
        'Indiana': 'Indianapolis',
        'Iowa': 'Des Moines',
        'Kansas': 'Topeka',
        'Kentucky': 'Frankfort',
        'Louisiana': 'Baton Rouge',
        'Maine': 'Augusta',
        'Maryland': 'Annapolis',
        'Massachusettes': 'Boston',
        'Michigan': 'Lansing',
        'Minnesota':  'Saint Paul',
        'Mississippi': 'Jackson',
        'Missouri': 'Jefferson City',
        'Montana': 'Helena',
        'Nebraska': 'Lincoln',
        'Nevada': 'Carson City',
        'New Hampshire': 'Concord',
        'New Jersey': 'Trenton',
        'New York': 'Albany',
        'New Mexico': 'Santa Fe',
        'North Carolina': 'Raleigh',
        'North Dakota': 'Bismark',
        'Ohio': 'Columbus',
        'Oklahoma': 'Oklahoma City',
        'Oregon': 'Salem',
        'Pennslyvania': 'Harrisburg',
        'Rhode Island': 'Providence',
        'South Carolina': 'Columbia',
        'South Dakota': 'Pierre',
        'Tennessee': 'Nashville',
        'Texas': 'Austin',
        'Utah': 'Salt Lake City',
        'Vermont': 'Montpelier',
        'Virginia': 'Richmond',
        'Washington': 'Olympia',
        'West Virginia': 'Charleston',
        'Wisconsin': 'Madison',
        'Wyoming': 'Cheyenne'}

    count = 0

    items = list(statedict.items())
    random.shuffle(items)

    for key, value in items: 

        state = key
        city = value

        cityinput = input('What is the capital of ' + state + '? ')

        if cityinput.lower() == city.lower(): 
            count += 1
            print("Your answer is correct")

        else: 
            print("The correct answer should be", city)

        print("The correct count is", count)


main()
