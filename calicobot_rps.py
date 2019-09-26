import random
import time

choices = ("rock", "paper", "scissors")

def start_rps():
    global player_choice
    print("I love playing this game! Alright!")
    time.sleep(2)
    print("Type \'exit\' at any time to stop the game.")
    time.sleep(1.5)
    print("At three, we both pick a choice!")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("3!")
    player_choice = input("Your choice: ")
    rock_paper_scissors()

def rps():
    global player_choice
    print("Again!")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("3!")
    player_choice = input("Your choice: ")
    rock_paper_scissors()

def rock_paper_scissors():
    calico_choice = random.choice(choices)
    if player_choice.lower() == "exit":
        print("Okay! Thanks for playing with me! This was fun!")
        time.sleep(2)
        return
    if calico_choice == "rock" and player_choice.lower() == "rock":
        print("I play... Rock! Oh, you too? It's a tie, then!")
    elif calico_choice == "paper" and player_choice.lower() == "paper":
        print("I chose paper! Aaaand, seems like we tied!")
    elif calico_choice == "scissors" and player_choice.lower() == "scissors":
        print("Scissors! Wait, you chose scissors too! It's a tie!")
    elif calico_choice == "rock" and player_choice.lower() == "paper":
        print("Rock! Oh, hey, you won this one!")
    elif calico_choice == "rock" and player_choice.lower() == "scissors":
        print("I go for... Rock! Oops, squished your scissors!")
    elif calico_choice == "paper" and player_choice.lower() == "rock":
        print("I go with paper this time! Zing! Got you there!")
    elif calico_choice == "paper" and player_choice.lower() == "scissors":
        print("Paper! Ow, don't cut me! I lose, I lose!")
    elif calico_choice == "scissors" and player_choice.lower() == "rock":
        print("Sciss-... Damn, lost this one. This is fun!")
    elif calico_choice == "scissors" and player_choice.lower() == "paper":
        print("Scissors! I win against paper! Yay!")
    else:
        print("That's not a valid choice! You need to pick either \'paper\', \'rock\' or \'scissors\'!")
    rps()
