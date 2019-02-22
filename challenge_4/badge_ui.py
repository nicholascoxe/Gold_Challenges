
import badge_repo

while True:
    print('MENU')
    user_input = input('1. Add a badge\n' + 
                       '2. Edit a badge\n' +
                       '3. List all badges\n> ')
# ADD BADGE
    if user_input == '1':
        badge_id = input('What is the badge ID?\n>')
        door = input('List a door that it needs access to:\n>')
        more_doors = input('Any other doors(y/n)?\n>')
    if input == 'y':
        door = input('List a door that it needs access to:\n>')
        badge_repo.add_badge(badge_id, door, more_doors)
    elif input == 'n':
        continue
        #Return to main menu after this
# UPDATE BADGE
    if user_input == '2':
        pass


# LIST ALL BADGES
    
    if user_input == '3':
        tmp_dict = badge_repo.get_badges()
        for key in tmp_dict.items():
            print(key)
exit()



