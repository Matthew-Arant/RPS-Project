import random


moves = ['rock', 'paper', 'scissors']


def validate_input(prompt, o1, o2, o3):
    while True:
        valid = input(prompt).lower()
        if valid == o1:
            return valid
        elif valid == o2:
            return valid
        elif valid == o3:
            return valid
        else:
            print("Please Enter rock, paper, or scissors.")


class Player:

    def __init__(self):
        self.their_move = "rock"

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.mymove = my_move
        self.their_move = their_move


class RandomPlayer(Player):

    def move(self):
        rmove = random.choice(moves)
        return rmove


class HumanPlayer(Player):

    def __init__(self):
        self.name = self

    def move(self):
        self.choice = validate_input("Rock, Paper, or Scissors:",
                                     "rock",
                                     "paper",
                                     "scissors")
        return self.choice


class CyclePlayer(Player):

    def __init__(self):
        self.moves = 0

    def move(self):
        cmove = moves[self.moves % 3]
        self.moves += 1
        return cmove


class MimmickPlayer(Player):

    def __init__(self):
        super().__init__()

    def move(self):
        return self.their_move


def beats(one, two):

    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1score = 0
        self.p2score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if move1 == move2:
            print("Tie!")
        elif beats(move1, move2) is True:
            print("Player 1 wins!")
            self.p1score += 1
        else:
            print("Player 2 wins!")
            self.p2score += 1
        print(f"Player 1 - {self.p1score}, Player 2 - {self.p2score}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_many_rounds(self):
        print("Game start!")
        for round in range(1, 8):
            print(f"Round {round}:")
            self.play_round()
        if self.p1score > self.p2score:
            print(f"The score is {self.p1score}"
                  f" to {self.p2score}. Player 1 wins the game!")
        elif self.p1score < self.p2score:
            print(f"The score is {self.p1score}"
                  f" to {self.p2score}. Player 2 wins the game!")
        else:
            print(f"The score is {self.p1score}"
                  f" to {self.p2score}. The game is a tie!")
        print("Game over!")

    def play_one_rounds(self):
        print("Game start!")
        self.play_round()
        if self.p1score > self.p2score:
            print(f"The score is {self.p1score}"
                  f" to {self.p2score}. Player 1 wins the game!")
        elif self.p1score < self.p2score:
            print(f"The score is {self.p1score}"
                  f" to {self.p2score}. Player 2 wins the game!")
        else:
            print(f"The score is {self.p1score}"
                  f" to {self.p2score}. The game is a tie!")
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_many_rounds()