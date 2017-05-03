

class Player():

    def __init__(self):

        self.name = 'Joe'
        self.age = 11
        
        # The most important thing in life:
        self.health = 100
        self.happiness = 50
        
        self.experience = 0
        self.knowledge = 0
        self.money = 0
        
        # School related
        self.math = 0
        self.physics = 0
        self.chemistry = 0
        self.biology = 0
        self.english = 0
        self.geography = 0
        self.history = 0
        self.computing = 10 # hehe
        
        self.days_attended = 0
        self.homework_missed = 0


def main():
    player = Player()
    print(player.health)

if __name__ == '__main__':
    main()
