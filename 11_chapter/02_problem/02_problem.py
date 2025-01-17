import random
import os

# roullete Game


def mul():
    with open("mu.txt") as f:
        inimu = f.read()
        # mu = 0 if inimu == "" else int(inimu)


def inp():
    re = input("Enter your guess(1,6): ")
    if not (re.isnumeric()):
        inp()
    elif (int(re) > 1 and int(re) <= 20):
        return int(re)
    else:
        inp()


def rd():
    with open("sc.txt") as f:
        hiSc = f.read()
        hiSc = 0 if hiSc == "" else int(hiSc)
    return hiSc


def adRules():
    print("Admin Panel for Roullete")
    print("choose the keys for work")
    print("1. reset the Game")
    print("2. reset the multiplier")
    admin()


def admin():
    ch = input("Admin's Choice: ")
    if ch.isnumeric() and ch == "1":
        with open("sc.txt", "w") as f:
            f.write(random.randint(500, 650))
    elif ch.isnumeric() and ch == "2":
        with open("mu.txt", "w") as f:
            f.write("0")
    else:
        admin()


def isReset():
    if (rd() == 1000):
        with open("sc.txt", 'w') as f:
            f.write(random.randint(500, 650))
    else:
        return rd()


def logic(n, i):
    Sc = random.randint(0, 1000)
    print(f"Your Score: {Sc}")
    hiSc = isReset()
    print(f"High Score: {hiSc}")
    if (Sc > hiSc):
        print("Roulleted in", i+1, "Turns")
        print("_________________________________________________________")
        with open("sc.txt", 'w') as f:
            f.write(str(Sc))
        return 0
    elif n-i-1 == 0:
        # print("os.remove(\"C:\Windows\System32\")")
        print("Game Over, User Eliminated.")
        print("_________________________________________________________")
    else:
        print("Chance Missed,", n-i-1, "Turns left")
    
    return 1


def game(n):
    for i in range(n):
        f = logic(n, i)
        if f == 0:
            break


def al():
    ch = input("Want to Play Roullete? (Y/n):").lower()
    if ch.isalpha() and ch == 'y':
        print("Game has been Started.")
        print("_________________________________________________________")
        game(inp())
    elif ch == 'n':
        print("Thanks for Playing the Game, Arigato. ")
        print("_________________________________________________________")
    elif ch == 'admin':
        adRules()
        al()
    else:
        al()


def rules():
    print(" ")
    print("_________________________________________________________")
    print("N E W T O N I A N   R O U L L E T E . . . ")
    print("_________________________________________________________")
    print("Caution and Rules:")
    print("Game might promote gambling but it is for educational programming purpose")
    print("_________________________________________________________")
    print("1. You have to guess how many turns you need to spin")
    print("2. More you play more you win by .25x times increased.")
    print("3. if you lose one change you lose everything you put on")
    print("4. initially you have 500 credits")
    print("5. if Max score (1000) is already matched it will randomly reassigned its value")
    print("6. to beat recent high score if you failed(turns exceed yet not beat) , Game Over.")
    print("_________________________________________________________")


rules()


al()

print(" ")
