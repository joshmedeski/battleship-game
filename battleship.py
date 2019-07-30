from board import Board
import numpy as np
import screen

# TODO add color with https://github.com/tartley/colorama

# Setup
screen.draw()
player_one_name = input("Player 1, enter your name: ")
player_one = Board(f'{player_one_name}', {
    'carrier': 'a4v',
    'battleship': 'b1h',
    'cruiser': 'f1h',
    'submarine': 'f2v',
    'destroyer': 'j5h'
})

screen.draw()
player_two_name = input("Player 2: enter your name: ")
player_two = Board(f'{player_two_name}', {
    'carrier': 'a4v',
    'battleship': 'b1h',
    'cruiser': 'f1h',
    'submarine': 'f2v',
    'destroyer': 'j5h'
})


def start():
    i = 0
    while player_one.progress() < 100 and player_two.progress() < 100:

        i += 1

        # temporary while-stop for development. remove for actual play
        if i > 2:
            print('iteration counter break.')
            break

        # Allow players to shoot at coordinates (tell system if hit or miss)
        # Josh Code

        # Sample for Jarrett's development. replace with Josh's code
        player_one.tracker = np.random.randint(0, 2, (10, 10))
        player_one.incoming_attacks = player_one.tracker

        player_two.tracker = np.random.randint(0, 2, (10, 10))
        player_two.incoming_attacks = player_two.tracker
        # /sample

        # feedback >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        print(f.renderText('Turn ' + str(i) + ':' + ' P1 board'))
        print(player_one)
        print('P1', player_one.fleet_audit(), '\n')

        print(f.renderText('Turn ' + str(i) + ':' + ' P2 board'))
        print(player_two)
        print('P2', player_two.fleet_audit(), '\n')

        print(' --- ')

        # End game when all battleships of one player are gone


start()

print("test 0==' '", 0 == ' ')

# Allow players to shoot at coordinates (tell system if hit or miss)
# End game when all battleships of one player are gone
