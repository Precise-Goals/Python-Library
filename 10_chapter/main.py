import random

convention = {}
convention.update({0: "Stone", 1: "Paper", 2: "Scissor"})
game = 0
user = 0
score = {
    "user": 0,
    "game": 0,
}


def line():
    print("--------------------------------------")

def Runs():
    while True:
        try:
            print(" ")
            line()
            print("| Stone, Paper & Scissor ")
            n = int(input("| How much Pointer's match you want: "))
            if n > 0:
                break
        except ValueError:
            print("Provide Numeric positive Value.")
    return n


def scoreBoard():
    print("|------------ ScoreBoard ------------|")
    print("| 0 : Stone     |   current scores   |")
    print("| 1 : Paper     |   user        pc   |")
    print("| 2 : Scissor   |   ", score["user"], end="")
    print("          ", score["game"], "  |")


def logic(ui, gi, u, g):
    if (ui > gi or (ui == 0 and gi == 2)):
        u += 1
        print("| User Takes the Point ______________|")
    else:
        g += 1
        print("| Computer Takes the Point __________|")
    print(" ")
    score.update({"user": u, "game": g})


def Game():
    scoreBoard()
    game_inp = random.randint(0, 2)
    user_inp = int(input("| Enter Choice: "))
    if ((user_inp >= 0) and (user_inp <= 2)):
        logic(user_inp, game_inp, score["user"], score["game"])
    else:
        print("Invalid Choice, select only 0,1 & 2")
        Game()


def Decide():
    isRegame = input("| Play Again ? let us know (Y/N): ").lower()
    if isRegame == 'y':
        print("| Game is Restarting ...")
        score.update({"user": 0, "game": 0})
        Start()
    elif isRegame == 'n':
        print("| Thanks for Playing, Arigato :)")
        line()
        print(" ")
        pass
    else:
        print("| Kindly answer in (Y/N).")
        Decide()


def Start():
    n = Runs()
    for i in range(n):
        Game()
    line()
    net = (score["game"]-score["user"]).__abs__()
    print("| User scored:", score["user"])
    print("| Computer scored:", score["game"])
    if (score["user"] > score["game"]):
        print("| User Claims the Victory by", net, " points.")
    elif (score["user"] < score["game"]):
        print("| Computer Claims the Victory by", net, "points.")
    else:
        print("Match is Tie, Damn Competition.")
    line()
    Decide()


Start()
