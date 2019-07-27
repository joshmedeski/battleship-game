from pyfiglet import Figlet
from board import Board

# Welcome message

f = Figlet(font='slant')
print('Welcome to')
print(f.renderText('Battleship'))

# Prompt user's names
print('Time to find a buddy and start playing.')
# player_one_name = input("Player 1: What's your name? ")
# player_two_name = input("Player 2: What's your name? ")

game_board = Board()
print(game_board.area)
print(game_board.matrix)

# Setup board for each player


# Allow players to shoot at coordinates (tell system if hit or miss)
# End game when all battleships of one player are gone
