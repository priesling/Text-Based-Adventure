

class Screen():

    TITLE = 'The Life of Joe'

    def __init__(self, text):

        self.text = text
        self.separator = '\n---------------------------------------\n'


    def display(self):

        print(self.separator)
        print(Screen.TITLE)
        print(self.separator)
        print(self.text)
        print(self.separator)

        return input('\t: ')


def main(args):
    pass

if __name__ == '__main__':
    main()
