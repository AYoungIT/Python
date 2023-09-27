# Name Ashley Young
# Date 10/8/22
# This program is a text based game about traveling through outerspace and encountering an alien predator

def main_menu():
    # Printing the instructions and welcoming the player
    print("Outer Space Alien Text Adventure Game")
    print("Collect 6 items to win the game, or be defeated by the Alien Predator")
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: get 'item name'")


def move_between_rooms(current_room, move, rooms):
    # moving between rooms
    current_room = rooms[current_room][move]
    return current_room


def get_item(current_room, move, rooms, inventory):
    # gathering items and adding to inventory
    inventory.append(rooms[current_room]['item'])
    del rooms[current_room]['item']


def main():
    # dictionary of rooms with items
    rooms = {
        'Crew Quarters': {'West': 'Bridge'},
        'Bridge': {'South': 'Galley', 'East': 'Crew Quarters', 'item': 'Smoke Bomb'},
        'Galley': {'West': 'Airlock', 'East': 'Exercise Room', 'South': 'Faraday Cage', 'item': 'Soup'},
        'Airlock': {'East': 'Galley', 'item': 'Cloaking Device'},
        'Exercise Room': {'North': 'Armory', 'West': 'Galley', 'item': 'Firstaid Kit'},
        'Armory': {'South': 'Exercise Room', 'item': 'Laser Gun'},
        'Faraday Cage': {'East': 'Plant Habitat', 'North': 'Galley', 'item': 'Teleport Device'},
        'Plant Habitat': ''
    }
    s = ' '
    # inventory list
    inventory = []
    # stating the starting room
    current_room = "Crew Quarters"
    # showing the main menu
    main_menu()

    while True:
        # winning when encountering the alien predator
        if current_room == 'Plant Habitat':
            # winning case
            if len(inventory) == 6:
                print('Congratulations you have defeated and obliterated the Alien Preadator!')
                print('Thank you for playing!')
                break
            # losing case due to not gathering all the items
            else:
                print('\nUh oh! You did not gather all of the items to defeat the Alien Predator!')
                print('You were killed by the Alien Predator')
                print('Thank you for playing!')
                break
        # Telling the user the current room they are in, their inventory and ask for a move, ignores case
        print('You are in the ' + current_room)
        print(inventory)
        # lets the player know if there is an item in the room
        if current_room != 'Plant Habitat' and 'item' in rooms[current_room].keys():
            print('You see the {}'.format(rooms[current_room]['item']))
        print('------------------------------')
        move = input('Enter your move: ').title().split()

        # if player moves to a different room
        if len(move) >= 2 and move[1] in rooms[current_room].keys():
            current_room = move_between_rooms(current_room, move[1], rooms)
            continue
        # if player gets an item
        elif len(move[0]) == 3 and move[0] == 'Get' and ' '.join(move[1:]) in rooms[current_room]['item']:
            print('You pick up the {}'.format(rooms[current_room]['item']))
            print('------------------------------')
            get_item(current_room, move, rooms, inventory)
            continue
        # input validation
        else:
            print('Invalid move, please try again')
            continue


main()
