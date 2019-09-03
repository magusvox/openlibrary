# Missions:
# [0] Main Mission  [1] Sub1    [2] Sub2    [3] Sub3
import random, operator

missions = ['Main mission']
allplayers = []
allplayerscount = 0
player = []
missioncount = 1
missions.insert(1, ('Sub mission', missioncount))
missioncount += 1
allplayers.insert(0, 'admin')
actualround = ['']

class Player():
    def __init__(self, name, race):
        self.name = name
        self.race = race
        self.level = 1
        self.num = allplayerscount
    def info(self):
        return f'{self.name} is a Lv{self.level} {self.race}'

def menu():
    title = 'RPG Manager'
    print(f"{'#' * 10} {title} {'#' * (40 - len(title))}")
    userinput = input('[1] History progress\n[2] Players\n[3] Tools\n[4] God tools\n[5] Exit\nChoose a option: ')
    if userinput == '1':
        progress()
    elif userinput == '2':
        playersmenu()
    elif userinput == '3':
        tools()
    elif userinput == '4':
        godmenu()
    elif userinput == '5':
        userinput = input('Are you sure? [Y] to confirm')
        if userinput.upper() == 'Y':
            exit()
        else:
            menu()
    else:
        print("Error: invalid input")
        menu()


def progress():
    title = 'History Progress'
    print(f"{'#' * 10} {title} {'#' * (40 - len(title))}")
    print(f"Active missions:\n{missions}")
    print(f'Players:\n{allplayers}')
    input("")
    menu()

def godmenu():
    title = 'God Menu'
    print(f"{'#' * 10} {title} {'#' * (40 - len(title))}")
    userinput = input(f"[1] Add mission\n[2] Add level to Player\n[4] Back to menu\nChoose a option: ")
    if userinput == '1':
        menu()
    elif userinput == '2':
        userinput = input("Enter player ID: ")
        try:
            print(f'Player: {player[int(userinput)].name} leveled from {player[int(userinput)].level} to {player[int(userinput)].level + 1}')
            player[int(userinput)].level += 1
            menu()
        except IndexError:
            print("Player not found.")
            menu()
    elif userinput == '4':
        menu()
    else:
        print("invalid input")
        menu()


def createplayer():
    global player, allplayers, allplayerscount
    createdplayer = Player(input("Player name: "), input("Race: "))
    allplayers.insert(allplayerscount, ('Player:', allplayerscount, "Name:" + createdplayer.name, "Race:", createdplayer.race))
    player.insert((allplayerscount + 1), '')
    player[allplayerscount] = createdplayer
    allplayerscount += 1
    print(f"Succesful! {createdplayer.name} is the Player N:{createdplayer.num}")
    menu()


def playersmenu():
    title = 'Players Menu'
    print(f"{'#' * 10} {title} {'#' * (40 - len(title))}")
    userinput = input('[1] Create new Player\n[2] Player stats\n[3] nsei\n[4] nsei\n[5] Exit\nChoose a option: ')
    if userinput == '1':
        createplayer()
    elif userinput == '2':
        userinput = input('Enter player ID: ')
        try:
            print(player[int(userinput)].info())
            menu()
        except IndexError:
            print("Player not found")
            menu()


def tools():
    global actualround
    title = 'Tools'
    print(f"{'#' * 10} {title} {'#' * (40 - len(title))}")
    userinput = input('[1] D20\n[2] D6\n[3] Actual round order\n[4] Get a Round\n[5] Back to menu\nChoose a option: ')
    if userinput == '1':
        print(f'The dices rolls... {random.randint(1, 20)}')
        tools()
    elif userinput == '2':
        print(f'The dices rolls... {random.randint(1, 6)}')
        tools()
    elif userinput == '3':
        print(f'Actual round in crescent order: {actualround}')
        tools()
    elif userinput == '4':
        try:
            userinput = input(f'Extra turns? {allplayerscount}+ ')
            turns = int(userinput) + allplayerscount
            round = []
            while turns > 0:
                userinput = input(f'Who is rolling the dice? [{turns}]: ')
                round.insert(turns, (userinput, random.randint(1, 20)))
                turns -= 1
                if userinput.upper() == 'EXIT':
                    print('Canceled')
                    tools()
            actualround = round
            print(sortuple(actualround))
            tools()
        except ValueError:
            print("If no extra turns, type 0")
            tools()
    elif userinput == '5':
        menu()
    else:
        print('Invalid input')
        menu()
    
def sortuple(tup):
    lst = len(actualround)
    for i in range(0, lst):
        for j in range(0, lst-i-1):
            if (actualround[j][1] > actualround[j + 1][1]):
                temptup = actualround[j]
                actualround[j] = actualround[j + 1]
                actualround[j + 1] = temptup
    return f'Actual round in crescent order: {actualround}'

menu()
