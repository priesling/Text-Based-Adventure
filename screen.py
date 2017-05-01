

class Screen():

    TITLE = 'The Life of Joe'

    def __init__(self):

        self.header = None
        self.questions = None
        self.prompt = None

        self.separator = '\n---------------------------------------\n'


    def display(self):

        print(self.separator)
        print(Screen.TITLE)
        print(self.separator)
        print(self.header)
        print(self.separator)
        print(self.questions)
        print(self.separator)

        return input(self.prompt)


def main(args):
    pass

if __name__ == '__main__':
    main()
