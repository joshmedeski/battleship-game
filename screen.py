from pyfiglet import Figlet
import os

game_title = Figlet('larry3d').renderText('Battleship')


def clear():
    os.system('clear')


board = '    a b c d e f g h i j \n  - - - - - - - - - - - -\n1 |                     |\n2 |                     |\n3 |                     |\n4 |                     |\n'


def draw():
    clear()
    print(game_title)
    print(board)
