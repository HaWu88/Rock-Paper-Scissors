#!/usr/bin/env python3
# Wu, Hamilton
import random
import sys

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class ReflectPlayer(Player):
    def move(self):
        if game.round == 1:
            return random.choice(moves)
        return self.their_move


class CyclePlayer(Player):
    def move(self):
        if game.round == 1:
            return random.choice(moves)
        index = 0
        for choice in moves:
            if choice == self.my_move:
                return moves[(index + 1) % 3]
            index += 1


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        # My Prompt for Input Validation
        prompt = "Please enter Rock, Paper, or Scissors: "
        choice = input_validate(prompt, moves)
        return choice


# input validation function
def input_validate(prompt, list_=None):
    while True:
        choice = input(prompt)
        # make input lowercase for check with list_
        choice = choice.lower()
        # End Game if Q or quit
        if choice == 'q' or choice == 'quit':
            print(f"\n** Final Score **\nPlayer 1: {game.p1_score}\n"
                  f"Player 2: {game.p2_score}\n")
            print("Thanks for playing. Have a Nice Day.")
            sys.exit()
        # incase of dev making their list_ in CAP
        list_ = [x.lower() for x in list_]
        # check if choice is not in list_
        if list_ is not None and choice not in list_:
            template = "** Input must be {}. **"
            # incase of dev making an empty list_
            if len(list_) == 1:
                print(template.format(*list_))
            # expected input from User
            else:
                expected = " or ".join((
                    ", ".join(str(x).capitalize() for x in list_[:-1]),
                    str(list_[-1]).capitalize()
                ))
                print(template.format(expected))
        else:
            return choice


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0
        self.tie = 0
        self.round = 1

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1.capitalize()}"
              f" Player 2: {move2.capitalize()}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        # Determine the Winner
        if beats(move1, move2):
            print(f"{'** PLAYER 1 WINS **' : >30}")
            self.p1_score += 1
        elif move1 == move2:
            print(f"{'** TIE **' : >25}")
            self.tie += 1
        else:
            print(f"{'** PLAYER 2 WINS **' : >30}")
            self.p2_score += 1
        # display score after each round
        print(f"Score: Player 1 [{self.p1_score}], Tie [{self.tie}]"
              f", Player 2 [{self.p2_score}]\n")

    def play_game(self):
        # Title Page
        print(f'{"**************************************": >50}')
        print(f'{"*  Welcome to Rock, Paper, Scissors! *": >50}')
        print(f'{"**************************************": >50}')
        quit_quote = "** Enter 'q' or 'quit' to End Game. **"
        print(f'{quit_quote: >50}')
        print(f'{"**************************************": >50}')
        # infinite loop playing rounds of RPS
        # until user uses q or quit in validation
        while True:
            print(f"Round {self.round}:")
            self.play_round()
            self.round += 1


if __name__ == '__main__':
    # implement all 3 Class into a really simple Computer Play
    rand = random.choice((CyclePlayer, RandomPlayer, ReflectPlayer))
    # remove rand() to your choice of Computer Player
    game = Game(HumanPlayer(), rand())
    game.play_game()
