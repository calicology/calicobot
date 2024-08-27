import time
import os

def wakeup():
    os.system('clear')
    bar = [
        "z..........",
        "Zz.........",
        "zZz........",
        "ZzZz.......",
        "ZZzZz......",
        "zZZzZz.....",
        ".zZZzZz....",
        "..zZZzZz...",
        "...zZZzZz..",
        "....zZZzZz.",
        ".....zZZzZz",
        "......zZZzZ",
        ".......zZZz",
        "........zZZ",
        ".........zZ",
        "..........z",
    ]
    i = 0

    while i < len(bar) * 2:
        print(bar[i % len(bar)], end="\r")
        time.sleep(.2)
        i += 1
    os.system('clear')
    sleeping()
    time.sleep(3)
    print("0% - Prepating calicomputation...")
    time.sleep(1.5)
    os.system('clear')
    sleeping()
    print("2% - Prepating calicomputation...")
    time.sleep(0.1)
    os.system('clear')
    sleeping()
    print("7% - Prepating calicomputation...")
    time.sleep(0.2)
    os.system('clear')
    sleeping()
    print("9% - Prepating calicomputation...")
    time.sleep(0.1)
    os.system('clear')
    sleeping()
    print("9% - Prepating calicomputation...")
    time.sleep(0.2)
    os.system('clear')
    sleeping()
    print("13% - Prepating calicomputation...")
    time.sleep(0.8)
    os.system('clear')
    sleeping()
    print("16% - Prepating calicomputation...")
    time.sleep(0.1)
    os.system('clear')
    sleeping()
    print("19% - Prepating calicomputation...")
    time.sleep(0.3)
    os.system('clear')
    sleeping()
    print("20% - Calibrating furry algorithms...")
    time.sleep(0.1)
    os.system('clear')
    sleeping()
    print("25% - Calibrating furry algorithms...")
    time.sleep(0.2)
    os.system('clear')
    sleeping()
    print("28% - Calibrating furry algorithms...")
    time.sleep(0.3)
    os.system('clear')
    sleeping()
    print("32% - Calibrating furry algorithms...")
    time.sleep(0.1)
    os.system('clear')
    sleeping()
    print("40% - Calibrating furry algorithms...")
    time.sleep(0.1)
    os.system('clear')
    sleeping()
    print("48% - Calibrating furry algorithms...")
    time.sleep(0.3)
    os.system('clear')
    sleeping()
    print("54% - Calibrating furry algorithms...")
    time.sleep(0.1)
    os.system('clear')
    sleeping()
    print("56% - Calibrating furry algorithms...")
    time.sleep(0.8)
    os.system('clear')
    sleeping()
    print("61% - Downloading latest english slang into Calico dictionaries...")
    time.sleep(0.2)
    os.system('clear')
    sleeping()
    print("68% - Downloading latest english slang into Calico dictionaries...")
    time.sleep(0.1)
    os.system('clear')
    sleeping()
    print("72% - Downloading latest english slang into Calico dictionaries...")
    time.sleep(0.3)
    os.system('clear')
    sleeping()
    print("79% - Downloading latest english slang into Calico dictionaries...")
    time.sleep(0.1)
    os.system('clear')
    sleeping()
    print("80% - Downloading latest english slang into Calico dictionaries...")
    time.sleep(0.3)
    os.system('clear')
    sleeping()
    print("84% - Downloading latest english slang into Calico dictionaries...")
    time.sleep(0.2)
    os.system('clear')
    sleeping()
    print("88% - Downloading latest english slang into Calico dictionaries...")
    time.sleep(0.4)
    os.system('clear')
    sleeping()
    print("90% - Preparing byte-sized treats...")
    time.sleep(0.1)
    os.system('clear')
    sleeping()
    print("91% - Preparing byte-sized treats...")
    time.sleep(0.2)
    os.system('clear')
    sleeping()
    print("94% - Preparing byte-sized treats...")
    time.sleep(0.5)
    os.system('clear')
    sleeping()
    print("97% - Preparing byte-sized treats...")
    time.sleep(0.1)
    os.system('clear')
    sleeping()
    print("98% - Preparing byte-sized treats...")
    time.sleep(0.2)
    os.system('clear')
    sleeping()
    print("99% - Preparing byte-sized treats...")
    time.sleep(4)
    os.system('clear')
    print("     x  |\__/|                               ")
    print("    ?  /_  . |        Waking up Calicobot...!")
    print("       \_^_   \  x                           ")
    print("        /CALICO\                             ")
    print(" ")
    print("...!")
    time.sleep(2)
    os.system('clear')
    wokeUp()

def sleeping():
    print("     z  |\__/| z                             ")
    print("    Z  /_  _ |        Waking up Calicobot... ")
    print("       \_^_   \  z                           ")
    print("     z  /CALICO\                             ")
    print(" ")

def wokeUp():
    wokeUpAnimation = [
        "    +   |\__/|  +\n     x /.  . |        Calicobot is awake!\n       \_^_   \ x\n    +   /CALICO\ \n ",
        "     x  |\__/| x\n    +  /.  . |        Calicobot is awake!\n       \_^_   \  +\n     x  /CALICO\ \n ",
    ]
    wokeUpIncrement = 0

    while wokeUpIncrement < 6:
        os.system('clear')
        print(wokeUpAnimation[wokeUpIncrement % len(wokeUpAnimation)])
        time.sleep(.5)
        wokeUpIncrement += 1
