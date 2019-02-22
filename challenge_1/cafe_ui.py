

import cafe

while True: 
    print('Welcome to Komodo Cafe Menu')
    user_input = input('1. Add an item to the Menu\n' + 
                       '2. View Menu items\n' +
                       '3. Delete an item on the Menu\n' + 
                       '4. Exit\n> ')
    
    # 1 ADDING ITEM TO MENU
    if user_input == '1':
        number = input('Enter Item Number: \n>') #figure out how to print statement (ID Number already in use) if number is already in use
        name = input('Enter Meal Name: \n>')
        ingredients = input('Enter Meal Ingredients: \n>')
        price = input('Enter Price: \n>')
        description = input('Give the Item a Description: \n>')
        cafe.add_item(number, name, ingredients, price, description)
    # 2 VIEW ALL ITEMS ON MENU
    elif user_input == '2':
        items = cafe.get_items()
        print(items)
    # 3 DELETE ITEM ON MENU
    elif user_input == '3':
        try:
            name_to_del = input('Enter Meal Name to Delete: ')
            cafe.delete_item(name)
        except Exception:
            print('Item does not exist. Please enter a valid item name:')
    # 4 EXIT APP
    elif user_input == '4':
        exit()
 