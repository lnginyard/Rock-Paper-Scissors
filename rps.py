import random
from random import randint
import time

# create a list of play options
t = ["Rock", "Paper", "Scissors"]

# assign a random play to the computer
computer = t[randint(0, 2)]


moves = ['rock', 'paper', 'scissors']


class Player:
    my_move = None
    their_move = None

    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            move = input("Rock, Paper, Scissors? (Type Quit to exit) ").lower()
            if move in moves:
                return move
            if move == 'quit':
                print('Bye!')
                exit(0)

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move
        return self.my_move


class ReflectPlayer(Player):
    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        else:
            return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        else:
            if self.my_move == 'rock':
                return 'paper'
            elif self.my_move == 'paper':
                return 'scissors'
            elif self.my_move == 'scissors':
                return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    p1_score = 0
    p2_score = 0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1 move: {move1}")
        time.sleep(2)
        print(f"Player 2 move: {move2}")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        if beats(move1, move2):
            self.p1_score += 1
            print("**PLAYER 1 WINS THE ROUND**")
        elif beats(move2, move1):
            self.p2_score += 1
            print("**PLAYER 2 WINS THE ROUND**")
        else:
            print("**TIE**")
            time.sleep(1)
        print(f"Player 1 score: {self.p1_score}")
        time.sleep(1)
        print(f"Player 2 score: {self.p2_score}")

    def play_game(self):
        print("Let's play Rock, Paper, Scissors!\n")
        time.sleep(1)
        print("The player that wins by 3 rounds wins the game!\n")
        for round in range(100):
            time.sleep(1)
            print(f"Round {round + 1}:")
            time.sleep(1)
            self.play_round()
<<<<<<< HEAD
            if self.p1_score > self.p2_score + 1:
                print("**PLAYER 1 WINS THE GAME!**")
                break
            if self.p2_score > self.p1_score + 1:
=======
            time.sleep(1)
            if self.p1_score > self.p2_score + 1:
                # pause for 2 seconds to allow the user to see the result
                time.sleep(1)
                # print("Player 1 wins the game!")
                print("**PLAYER 1 WINS THE GAME!**")
                break
            if self.p2_score > self.p1_score + 1:
                time.sleep(1)
>>>>>>> 79a12b4f47f1a94325c9b95aa756cb48baf978ac
                print("**PLAYER 2 WINS THE GAME!**")
                break
        print("The final score is: ")
        time.sleep(1)
        print(f"Player 1: {self.p1_score}")
        time.sleep(1)
        print(f"Player 2: {self.p2_score}")
        time.sleep(1)
        print("Game over!")


if __name__ == '__main__':
    players = [
        Player(),
        RandomPlayer(),
        ReflectPlayer(),
        CyclePlayer()
    ]
    p1 = HumanPlayer()
    p2 = random.choice(players)
    game = Game(p1, p2)
    game.play_game()
# class HumanPlayer(player):
    #
    # ask player to choose play
    # while player == False:
    # player = input("Rock, Paper, Scissors?"
    #               "(Type Quit to exit) ").lower()
    # if t in ts:
    #    return t
    #    if move == 'quit':
    #        print('Bye!')
    #    exit(0)
    # if player in t:
    #    print("Player chooses", player)
    #    player = True
    # else:
    #    print("Invalid input")
    #    player = False

    # display computer play
    # print("Computer chooses", computer)

    # compare player and computer play
    # if player == computer:
    #    print("It's a tie!")

    # elif player == "Rock":
    #    if computer == "Paper":
    #        print("Computer wins!")
    #    else:
    #        print("Player wins!")

    # elif player == "Paper":
    #    if computer == "Scissors":
    #        print("Computer wins!")
    #    else:
    #        print("Player wins!")

    # elif player == "Scissors":
    #    if computer == "Rock":
    #        print("Computer wins!")
    #    else:
    #        print("Player wins!")


# while player == False:
    # set player to True
    #player = input("Rock, Paper, Scissors?")
    # if player == computer:
    #   print("Tie!")
    # elif player == "Rock":
    # if computer == "Paper":
    #     print("You lose!", computer, "covers", player)
    #  else:
    #       print("You win!", player, "smashes", computer)
    # elif player == "Paper":
    # if computer == "Scissors":
    #      print("You lose!", computer, "cut", player)
    # else:
    #       print("You win!", player, "covers", computer)
    # elif player == "Scissors":
    # if computer == "Rock":
    #      print("You lose...", computer, "smashes", player)
    #   else:
    #        print("You win!", player, "cut", computer)
    # else:
    #    print("That's not a valid play. Check your spelling!")
    # player was set to True, but we want it to be False so the loop continues
    #player = False
    #computer = t[randint(0, 2)]


# cpu's move

    # moves = ['rock', 'paper', 'scissors']

    # class Player:
    # my_move = None
    # their_move = None

    # def move(self):
    # return 'rock'

    # def learn(self, my_move, their_move):
    # self.my_move = my_move
    # self.their_move = their_move
    # return self.my_move, self.their_moves

    # class RandomPlayer(Player):
    # def move(self):
    # return random.choice(moves)

    # class HumanPlayer(Player):
    # def learn(self, my_move, their_move):
    # self.my_move = my_move
    # self.their_move = their_move
    # return self.my_move, their_move

    # class ReflectPlayer(Player):
    # def move(self):
    # if self.their_move is None:
    # return random.choice(moves)
    # else:
    # return self.their_move

    # def learn(self, my_move, their_move):
    # self.their_move = their_move

    # class CyclePlayer(Player):
    # def move(self):
    # if self.my_move is None:
    # return random.choice(moves)
    # else:
    # if self.my_move == 'rock':
    # return 'paper'
    # elif self.my_move == 'paper':
    # return 'scissors'
    # elif self.my_move == 'scissors':
    # return 'rock'

    # def learn(self, my_move, their_move):
    # self.my_move = my_move

    # def beats(one, two):
    # return ((one == 'rock' and two == 'scissors') or
    # (one == 'scissors' and two == 'paper') or
    # (one == 'paper' and two == 'rock'))

    # class Game:
    # p1_score = 0
    # p2_score = 0

    # def __init__(self, p1, p2):
    # self.p1 = p1
    # self.p2 = p2

    # def play_round(self):
    # move1 = self.p1.move()
    # move2 = self.p2.move()
    # print(f"Player 1 move: {move1}")
    # print(f"Player 2 move: {move2}")

    # self.p1.learn(move1, move2)
    # self.p2.learn(move2, move1)

    # if beats(move1, move2):
    # self.p1_score += 1
    # print("**PLAYER 1 WINS THE ROUND**")
    # elif beats(move2, move1):
    # self.p2_score += 1
    # print("**PLAYER 2 WINS THE ROUND**")
    # else:
    # print("**TIE**")
    # print(f"Player 1 score: {self.p1_score}")
    # print(f"Player 2 score: {self.p2_score}")

    # if __name__ == '__main__':
    # players = [
    # Player(),
    # RandomPlayer(),
    # ReflectPlayer(),
    # CyclePlayer()
    # ]
    # p1 = HumanPlayer()
    # p2 = random.choice(players)
    # game = Game(p1, p2)
    # game.play_game()
