import random
import sys


class Config:
    def __init__(self):
        self.codesize = 4
        self.maxattempt = 10
        self.color = 8
        self.Duplicates = False

    @property
    def ans(self):
        return self.__ans

    @ans.setter
    def ans(self, new_ans):
        self.__ans = new_ans.split()

    def __repr__(self):
        return str(self.__ans)

    __str__ = __repr__


class Game:
    def __init__(self):
        self.input = ['-99', '-99', '-99', '-99']
        self.win = False
        self.attempts = 0
        self.answer = self.generate_ans()
        self.guess_history = ['' for i in range(Settings.maxattempt)]
        self.check_history = ['' for i in range(Settings.maxattempt)]

    def check(self):
        check = []
        for index, val in enumerate(self.answer):
            guess = self.input.split()
            if val in guess:
                if index == guess.index(val) or val == guess[index]:
                    check += ['*']
                else:
                    check += ['o']

        if check == list('****'):
           self.win = True
        self.check_history.insert(0, ''.join(check))
        self.attempts += 1

    def take_input(self):
        while True:
            _guess = input()
            if _guess == 'Q':
                break
            elif len(_guess.split()) != Settings.codesize:
                print(f"-----Please enter {Settings.codesize} number separated by space(' '), or quit by typing ('Q')-----")
            else: break
        self.input = _guess
        self.guess_history.insert(0, [' '.join(_guess.split())])

    def generate_ans(self):
        _ans = []
        while len(_ans) != Settings.codesize:
            num = str(random.randint(1, Settings.color))
            if num not in _ans or Settings.Duplicates:
                _ans += [num]
        return _ans

    def GameScreen(self):
        padding = Settings.codesize*2
        print(f"{"="*8} || {"="*8}")
        for i in range(Settings.maxattempt):
            print(f"{''.join(self.guess_history[i]): <{padding}} || {' '.join(self.check_history[i]) : <{padding}}")

    def remove_duplicate(self, lists):
        return_list = []
        for i in lists:
            if i not in return_list:
                return_list += [i]
        return return_list

class GameController:
    def __init__(self):
        self.Menu_Run()

    def Game_Run(self):
        game = Game()
        self.ClearScreen()
        while not game.win:
            #print(game.answer)
            self.ClearScreen()
            game.GameScreen()
            print(game.answer)
            # Input Loop
            game.take_input()
            game.check()
            if game.input == 'Q':
                break

            if game.attempts > Settings.maxattempt-1:
                print("You exceeded max attempt, Game Lost.")
                print(game.answer)
                break
            elif game.win:
                print("Congrats")
        self.Menu_Run()

    def Menu_Run(self):
        while True:
            self.ClearScreen()
            response = input("1. Play\n"
                             "2. Settings\n"
                             "3. Exit\n")
            if response == '1':
                self.Game_Run()
            elif response == '2':
                self.Settings_Run()
            elif response == '3':
                sys.exit()

    def Settings_Run(self):
        self.ClearScreen()
        while True:
            response = input("1. Max Attempt\n"
                             "2. Code Size\n"
                             "3. Number of Colors\n"
                             "4. Duplicates Allowed [Y/N]\n"
                             "('Q') to quit\n")
            if response == '1':
                while True:
                    _input = int(input("Change Max Attempt to: "))
                    if _input > 0:
                        Settings.maxattempt = _input
                        break
            elif response == '2':
                while True:
                    _input = int(input("Change Codesize to (1- 10): "))
                    if _input in range(1, 11):
                        Settings.codesize = _input
                        break
            elif response == '3':
                while True:
                    _input = int(input("Change number of colors (1-8):"))
                    if _input in range(1, 9):
                        Settings.color = _input
                        break
            elif response =='4':
                while True:
                    _input = input("Duplicates Allowed [Y/N]:")
                    if _input == "Y":
                        Settings.Duplicates = True
                        break
                    elif _input == "N":
                        Settings.Duplicates = False
                        break
                    else:
                        print("Please input (Y/N)")
            elif response == 'Q':
                break

            self.ClearScreen()
        self.Menu_Run()
    def ClearScreen(self):
        for i in range(25):
            print()


# Game setup
Settings = Config()

# Game Loop
gameController = GameController()


