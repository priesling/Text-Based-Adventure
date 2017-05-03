
import csv

from player import Player
from screen import Screen


def display_initial_screen():


    with open('initial_screen.txt', 'r') as screen_data:
        contents = screen_data.read()
        initial_screen = Screen(contents)

    return initial_screen.display() 
        
    


def main():

    player = Player()
    player.name = display_initial_screen()

if __name__ == '__main__':

    main()
