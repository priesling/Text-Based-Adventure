

class Player():

    def __init__(self):

        self.name = 'Joe'
        # The most important thing in life:
        self.health = 100
        self.happiness = 50
        self.wealth = 0


def main():
    player = Player()
    print(player.health)

if __name__ == '__main__':
    main()
