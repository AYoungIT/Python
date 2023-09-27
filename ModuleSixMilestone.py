# name Ashley Young
# date 10/1/22
# this program allows a user to move between rooms or exit the program

# starting the game and defining main menu
def main_menu():
    print('\nWelcome to the Moving Between Rooms game')
    print('Move Commands: go North, go South, go West, go East')

# moving between rooms
def move_between_rooms(current_room, move, rooms):
    current_room = rooms[current_room][move]
    return current_room

# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.
rooms = {
    'Great Hall': {'South': 'Bedroom'},
    'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
    'Cellar': {'West': 'Bedroom'}
}

# defining the starting room
def main():
    s = ' '
    inventory = []
    current_room = 'Great Hall'
    main_menu()

    while current_room != 'exit': # starting the loop with exit ability
        print('You are in the ' + current_room)
        print('---------------------------')
        move = input('Enter your move: ').title().split() # asking for input from player
        if len(move) >= 2 and move[0].lower() == 'go' and move[1].capitalize() in rooms[current_room].keys():
            current_room = move_between_rooms(current_room, move[1].capitalize(), rooms)
            continue
        elif len(move) == 1 and move[0].lower() == 'exit': # allowing player to exit game
            current_room = 'exit'
        else:
            print('That is not a valid direction') # input validation

main()