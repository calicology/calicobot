# This was done with the help of Al Sweigart's book 'Invent Your
# Own Computer Games with Python' (Chapter 10).

import random
import time

coin = ("tails", "heads")

def ttt_board(position):
    print("+++++++++++++++++")
    print("+               +")
    print("+   "+position[1]+ " | "+position[2]+" | "+position[3]+"   +")
    print("+  ---+---+---  +")
    print("+   "+position[4]+ " | "+position[5]+" | "+position[6]+"   +")
    print("+  ---+---+---  +")
    print("+   "+position[7]+ " | "+position[8]+" | "+position[9]+"   +")
    print("+               +")
    print("+++++++++++++++++")

def start_ttt():
    print("Sweet! This game is fun!")
    time.sleep(2)
    print("I'm still learning, but I think I'm getting pretty good at it.")
    time.sleep(2)
    print("Alright, this is the board and the positions:")
    time.sleep(1)
    print("+++++++++++++++++")
    print("+               +")
    print("+   1 | 2 | 3   +")
    print("+  ---+---+---  +")
    print("+   4 | 5 | 6   +")
    print("+  ---+---+---  +")
    print("+   7 | 8 | 9   +")
    print("+               +")
    print("+++++++++++++++++")
    time.sleep(2)
    print("When you want to make a move, just type the number of the position you want!")
    time.sleep(3)
    return ttt()

# Possible patterns to win. Return True if one of those conditions is True.
def win_conditions(position, letter):
    return ((position[1] == letter and position[2] == letter and position[3] == letter) or
    (position[4] == letter and position[5] == letter and position[6] == letter) or
    (position[7] == letter and position[8] == letter and position[9] == letter) or
    (position[1] == letter and position[4] == letter and position[7] == letter) or
    (position[2] == letter and position[5] == letter and position[8] == letter) or
    (position[3] == letter and position[6] == letter and position[9] == letter) or
    (position[1] == letter and position[5] == letter and position[9] == letter) or
    (position[3] == letter and position[5] == letter and position[7] == letter))

# Prompt asking for the letter of the player - returns the list that is going
# to define user_letter and calico_letter.
def x_or_o():
    choice = ""
    print("So, you wanna be X or O?")
    choice = input("Your choice: ").lower()
    if choice == "x":
        return ["X", "O"]
    elif choice == "o":
        return ["O", "X"]
    else:
        print("That's not a valid choice! Just type 'x' or 'o'.")
        return x_or_o()

# Coin toss for who goes first.
def first_player():
    flip_coin = random.choice(coin)
    if flip_coin == "heads":
        return "Heads"
    else:
        return "Tails"

# Function to determine whether that position is free. Will be True if it's
# empty, will return False if it's not.
def check_free_position(board, move):
    return board[move] == " "

# Function that makes the empty position have the letter from the move.
def move_to_position(board, letter, move):
    board[move] = letter

# Function to capture the player's move. Turns the string input into an integer.
def user_turn(board):
    move = " "
    print("It's your turn! What position do you wanna go for?")
    move = input("Your move: ")
    if move not in "1 2 3 4 5 6 7 8 9".split():
        print("That's not a valid position! You need to type a number between 1 and 9.")
        time.sleep(1)
        return user_turn(board)
    elif check_free_position(board, int(move)) == False:
        print("That position is taken! You need to take a different one.")
        time.sleep(1)
        return user_turn(board)
    return int(move)

# Function to chose a random position from a list of possible positions in
# the AI algorithm
def calico_random_move(board, move_list):
    possible_moves = []
# Appends open positions in move_list to possible_moves
    for move in move_list:
        if check_free_position(board, move):
            possible_moves.append(move)
    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
# None of the moves in move_list are possible moves.
        return None

# Function to allow the AI algorithm to make predictions through copies of
# the board
def copy_board(board):
    copied_board = []
    for i in board:
        copied_board.append(i)
    return copied_board

def calico_turn(board, calico_letter):
    if calico_letter == "X":
        user_letter = "O"
    else:
        user_letter = "X"
# Checks if Calicobot can fill one of the win_conditions with the next move
    for i in range(1, 10):
        copy = copy_board(board)
        if check_free_position(copy, i):
            move_to_position(copy, calico_letter, i)
            if win_conditions(copy, calico_letter):
                return i
# Checks if Calicobot can prevent the user from filling one of the
# win_conditions in their next move
    for i in range(1, 10):
        copy = copy_board(board)
        if check_free_position(copy, i):
            move_to_position(copy, user_letter, i)
            if win_conditions(copy, user_letter):
                return i
# Corners first, more winning patterns
    move = calico_random_move(board, [1, 3, 7, 9])
    if move != None:
        return move
    if check_free_position(board, 5):
        return 5
# Fallback to sides
    return calico_random_move(board, [2, 4, 6, 8])

# Is true if there are no more free positions (game is a tie)
def tie(board):
    for i in range(1, 10):
        if check_free_position(board, i):
            return False
    return True

# Function returns True if the player says something like 'yes' or 'yeah'.
def play_again():
    print("Wanna play again?")
    return input("Your reply: ").lower().startswith("y")

def ttt():
# Empty board
    current_board = [" "] * 10
# Fetch the letters
    user_letter, calico_letter = x_or_o()
# Decide who goes first
    turn = first_player()
    print("Let's flip a coin to decide who goes first.")
    time.sleep(2)
    print("If it's heads, I go first. If it's tails, you go first. Deal?")
    time.sleep(2)
    print("Alright!")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("...")
    if turn == "Heads":
        print("And it's... {}! I go first!".format(turn))
    else:
        print("And it's... {}! You go first!".format(turn))
    time.sleep(2)
# Game starts!
    game_ongoing = True
    while game_ongoing:
# The user's turn
        if turn == "Tails":
            ttt_board(current_board)
            move = user_turn(current_board)
            move_to_position(current_board, user_letter, move)
            if win_conditions(current_board, user_letter):
                ttt_board(current_board)
                time.sleep(1)
                print("You won! You're so good at this game!")
                time.sleep(2)
                game_ongoing = False
            else:
                if tie(current_board):
                    ttt_board(current_board)
                    time.sleep(1)
                    print("Ohh, it's a tie!")
                    break
                else:
                    time.sleep(1)
                    print("Calicobot is thinking...")
                    time.sleep(2)
                    turn = "Heads"
# Calicobot's turn
        else:
            move = calico_turn(current_board, calico_letter)
            move_to_position(current_board, calico_letter, move)
            if win_conditions(current_board, calico_letter):
                ttt_board(current_board)
                time.sleep(1)
                print("I win this one! Yay!")
                time.sleep(2)
                game_ongoing = False
            else:
                if tie(current_board):
                    ttt_board(current_board)
                    time.sleep(1)
                    print("Look! It's a tie!")
                    break
                else:
                    turn = "Tails"
# Go back to ttt() if the player wants to play again, else quit
    if play_again() == True:
        return ttt()
    else:
        print("Okay! Thanks for playing with me! This was fun!")
        time.sleep(2)
        return
