
import csv

from player import Player
from screen import Screen


def display_initial_screen():

    initial_screen = Screen()

    with open('initial_screen.csv') as screen_data:

        contents = screen_data.readlines()

        header = contents[0].split(':=:')[1]
        questions = contents[1].split(':=:')[1]
        prompt = contents[2].split(':=:')[1]
        
        initial_screen.header = header
        initial_screen.questions = questions
        initial_screen.prompt = prompt

    return initial_screen.display() 
        
    


def main():

    player = Player()
    player.name = display_initial_screen()

if __name__ == '__main__':

    main()
