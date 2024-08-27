import calicobot_wakeup as wakeup
import time
import os

def start():
    wakeup.wakeup()
    time.sleep(2)
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

start()
