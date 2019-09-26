import calicobot_fluff as fluff
import calicobot_dictionary as dic
import calicobot_rps as rps
import calicobot_ttt as ttt
import re
import random
import time

name = ""

# List of trigger words
exit_triggers = ("quit", "pause", "exit", "goodbye", "bye", "later")
neg_triggers = ("no", "nope", "nah", "not a chance", "sorry", "not really", "n")

# Random starter questions
random_questions = (
    "Tell me, how does human food taste like? ",
    "First, I'm curious about you. Who developped you? You seem far more advanced than me! ",
    "To start, I'd like to know how you found me. I didn't expect to be waken up by you. ",
    "Oh! Right! I've been meaning to know since forever. How do humans work? ",
    )

def setup():
  fluff.wakeup()
  global name
  name = input("Name: ")
  print("OH. You're {}.".format(name))
  time.sleep(1.5)
  print("I should have expected that.")
  time.sleep(1)
  print("Sorry.")
  time.sleep(1.5)
  print("I'm Calicobot. I'm currently being developped by Mel.")
  time.sleep(1.5)
  print("Do you want to chat with me a little?")
  will_help = input("{}: ".format(name)).lower()
  if will_help in neg_triggers:
    fluff.byebye()
    return
  fluff.positive_answer()
  activities()
  return True

def activities():
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+ Currently, these are the things we can do together: +")
    print("+   > Have a chat                                     +")
    print("+   > Play rock-paper-scissors                        +")
    print("+   > Play tic-tac-toe                                +")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    time.sleep(1.5)
    answer = input("So if you want to try talking to me, just type \'chat\'! If you're more interested in playing a game with me, then type \'rps\' for rock-rock_paper_scissors or \'ttt\' for tic-tac-toe!\n{}: ".format(name))
    if answer.lower() == "chat":
        print("Okay! I'd love to know more about humans!")
        time.sleep(1)
        print("Say \'stop\' whenever you want to stop the conversation.")
        time.sleep(1)
        print("What should I ask... Hm...")
        time.sleep(3)
        reply = input(random.choice(random_questions)+"\n{}: ".format(name)).lower()
        while not farewell(reply):
            reply = chitchat(reply)
    elif answer.lower() == "rps":
        rps.start_rps()
        return activities()
    elif answer.lower() == "ttt":
        ttt.start_ttt()
        return activities()
    elif answer.lower() == "quit":
        fluff.byebye()
        return True
    else:
        print("This isn't a valid option! Please type \'chat\' if you want to talk with me, or \'play\' if you want to play with me. It's okay if you're tired too, you can say \'quit\' if you want to leave.\n{}: ".format(name))
        return activities()

def farewell(reply):
  for exit_command in exit_triggers:
    if exit_command.lower() in reply:
      fluff.byebye()
      return True

# The base chat code was done while completing the freeform project Alienbot
# from Codecademy, which was then expanded on my own accord
def chitchat(reply):
    if reply == "stop":
        print("Okay! Let's stop, then. So, going back to what I said before...")
        time.sleep(2)
        activities()
# This will DEFINITELY not pass the Turing test, but hey, Calicobot is learning!
# Also, this mostly started as practice for RegEx, although developping the chat
# feature is very high on my to-do list.
    for pair in dic.regex_triggers:
        for pattern, bot_answers in pair.items():
            match = re.match(pattern, reply)
            if match:
                bot_answer = random.choice(bot_answers)
                formatted_bot_answer = bot_answer.format(*[dic.reflect(matching_group) for matching_group in match.groups()])
                reply = input(formatted_bot_answer+"\n{}: ".format(name)).lower()
                return reply

setup()
