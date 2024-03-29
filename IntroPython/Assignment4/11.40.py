#Write a program that repeatedly prompts the user to enter a capital for a state.
# Upon receiving the user input, the program reports whether the answer is correct.
# Assume that 50 states and their capitals are stored in a two-dimensional list, as shown in Figure 11.13.
# The program prompts the user to answer all the states’ capitals and displays the total correct count.
# The user’s answer is not case sensitive. Implement the program using a list to represent the data in the following table.


def main():

    statearray = [
        ['Alabama', 'Montgomery'],
        ['Alaska', 'Juneau'],
        ['Arizona', 'Phoenix'],
        ['Arkansas', 'Little Rock'],
        ['California', 'Sacramento'],
        ['Colorado', 'Denver'],
        ['Connecticut', 'Hartford'],
        ['Delaware', 'Dover'],
        ['Florida', 'Tallahassee'],
        ['Georgia', 'Atlanta'],
        ['Hawaii', 'Honolulu'],
        ['Idaho', 'Boise'],
        ['Illinois', 'Springfield'],
        ['Indiana', 'Indianapolis'],
        ['Iowa', 'Des Moines'],
        ['Kansas', 'Topeka'],
        ['Kentucky', 'Frankfort'],
        ['Louisiana', 'Baton Rouge'],
        ['Maine', 'Augusta'],
        ['Maryland', 'Annapolis'],
        ['Massachusetts', 'Boston'],
        ['Michigan', 'Lansing'],
        ['Minnesota', 'Saint Paul'],
        ['Mississippi', 'Jackson'],
        ['Missouri', 'Jefferson City'],
        ['Montana', 'Helena'],
        ['Nebraska', 'Lincoln'],
        ['Nevada', 'Carson City'],
        ['New Hampshire', 'Concord'],
        ['New Jersey', 'Trenton'],
        ['New York', 'Albany'],
        ['New Mexico', 'Santa Fe'],
        ['North Carolina', 'Raleigh'],
        ['North Dakota', 'Bismark'],
        ['Ohio', 'Columbus'],
        ['Oklahoma', 'Oklahoma City'],
        ['Oregon', 'Salem'],
        ['Pennslyvania', 'Harrisburg'],
        ['Rhode Island', 'Providence'],
        ['South Carolina', 'Columbia'],
        ['South Dakota', 'Pierre'],
        ['Tennessee', 'Nashville'],
        ['Texas', 'Austin'],
        ['Utah', 'Salt Lake City'],
        ['Vermont', 'Montpelier'],
        ['Virginia', 'Richmond'],
        ['Washington', 'Olympia'],
        ['West Virginia', 'Charleston'],
        ['Wisconsin', 'Madison'],
        ['Wyoming', 'Cheyenne']]

    count = 0

    for i in range(len(statearray)):

        state = statearray[i][0]
        city = statearray[i][1]

        cityinput = input('What is the capital of ' + state + '? ')

        if cityinput.lower() == city.lower():
            count += 1
            print("Your answer is correct")
        else:
            print("The correct answer should be", city)

        print("The correct count is", count)


main()


