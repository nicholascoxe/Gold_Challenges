
import outing


while True: 
    print('*Komodo Outings*')
    user_input = input('1. List of Outings\n' +
                       '2. Add an Outing\n' +
                       '3. Calculate Total Costs\n' +
                       '4. Calculate Costs by Outing Type\n' +
                       '5. Exit\n> ')
#  1 PRINTS LIST OF ALL OUTINGS 
    if user_input == '1':
        outings = outing.get_outings()
        print(outings)
# 2 ADD OUTING
    elif user_input == '2':
        outing_type = input('Enter Outing type: \n')
        attending = input('Enter Number in Attendance: \n')
        date = input('Enter the Date: \n')
        cost_per_person = input('Enter cost per person: \n')
        total_cost = input('Enter Total cost of Outing: \n')
        outing.add_outing(outing_type, attending, date, cost_per_person, total_cost)
# 3 CALCULATE TOTAL COST OF OUTINGS 
    elif user_input == '3':
        pass
        # tried adding the strings and also changning them to int
        # adds all outing together
#   4 CALC COSTS BY OUTING TYPES
    elif user_input == '4':
            pass
        # couldnt figure this out
# 5 EXITS APP
    elif user_input == '5':
        exit()
    else:
        print('Please enter a valid function.')
