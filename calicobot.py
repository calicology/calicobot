import calicobot_wakeup as wakeup
import calicobot_rps as rps
import calicobot_ttt as ttt
import time
import os

def start():
    wakeup.wakeup()
    time.sleep(2)
    start_menu()

def start_menu():
    os.system('clear')
    print("        |\__/|     ")
    print("       /.  . |        What can Calicobot help you with?")
    print("       \_^_   \    ")
    print("        /CALICO\   ")
    print("")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("+  List of available options:              +")
    print("+    A > Learn about Calicobot             +")
    print("+    B > Personal Assistant                +")
    print("+    C > Study                             +")
    print("+    D > Play Games                        +")
    print("+    E > Exit Calicobot Script             +")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("")
    choice = input("Enter option: ").capitalize()

    match choice:
        case "A":
             print("Choice A")
        case "B":
             print("Choice B")
        case "C":
             print("Choice C")
        case "D":
             games_prompt()
        case "E":
             print("Bai bai~")
             quit()
        case _:
            os.system('clear')
            print("        |\__/|     ")
            print("       />  < |        Please enter a valid option!")
            print("       \_^_   \    ")
            print("        /CALICO\   ")
            time.sleep(2)
            start_menu()

def games_prompt():
    games_animation = [
        "    +   |\__/|  +\n     x /^  ^ |        Yay! I love games!\n       \_^_   \ x\n    +   /CALICO\ \n ",
        "     x  |\__/| x\n    +  /^  ^ |        Yay! I love games!\n       \_^_   \  +\n     x  /CALICO\ \n ",
    ]
    games_animation_increment = 0

    while games_animation_increment < 6:
        os.system('clear')
        print(games_animation[games_animation_increment % len(games_animation)])
        time.sleep(.5)
        games_animation_increment += 1

    time.sleep(1)
    games_menu()

def games_menu():
    os.system('clear')
    print("     x  |\__/| x\n    +  /^  ^ |\n       \_^_   \  +\n     x  /CALICO\ \n ")
    print("")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("+  What would you like to play?:           +")
    print("+    A > Play Tic-tac-toe                  +")
    print("+    B > Play Rock-Paper-Scissors          +")
    print("+    C > Go back to previous menu          +")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("")
    choice = input("Enter option: ").capitalize()

    match choice:
        case "A":
             ttt.start_ttt()
             games_menu()
        case "B":
             rps.start_rps()
             games_menu()
        case "C":
             start_menu()
        case _:
            os.system('clear')
            print("        |\__/|     ")
            print("       />  < |        Please enter a valid option!")
            print("       \_^_   \    ")
            print("        /CALICO\   ")
            time.sleep(2)
            games_menu()

start()
