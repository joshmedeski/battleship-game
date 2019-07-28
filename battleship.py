from pyfiglet import Figlet
from board import Board

# Welcome message

f = Figlet(font='slant')
print('Welcome to')
print(f.renderText('Battleship'))

# Prompt user's names
print('Time to find a buddy and start playing.')
player_one_name = input("What's your name, player 1? ")
player_one = Board(f'{player_one_name}', {
    'carrier': 'a4v',
    'battleship': 'b1h',
    'cruiser': 'f1h',
    'submarine': 'f2v',
    'destroyer': 'j5h'
})
# player_two_name = input("Player 2: What's your name? ")

# while True:
# if game over
#   end
# else
#   player 1 chooses
#   player 2 chooses

# Allow players to shoot at coordinates (tell system if hit or miss)
# End game when all battleships of one player are gone
