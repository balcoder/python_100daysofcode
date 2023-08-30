''' Check if guess is in the 50_states and write to map
    keep track of correct guess and number of correct answers '''
import pandas

DATA = pandas.read_csv("day25/50_states.csv")

class Guess:
    ''' Store guess data and update'''
    def __init__(self):
        self.data = DATA
        self.guess = ""
        self.correct = False
        self.score = 0
        self.correct_guess = []

    def check_guess(self, guess):
        ''' check guess and update if correct '''
        self.guess = guess
        if self.guess not in self.correct_guess:
            for state in DATA["state"]:
                if state == guess:
                    self.score += 1
                    self.correct_guess.append(state)
                    self.correct = True
        else:
            return False
    def get_coords(self, state):
        ''' get coordinates given the state name '''
        row = DATA[DATA.state == state]
        if not row.empty:
            x_coord = int(row.x.iloc[0])
            y_coord = int(row.y.iloc[0])
            return x_coord, y_coord
        else:
            return None
        