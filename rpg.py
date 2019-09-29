# Missions:
# [0] Main Mission  [1] Sub1    [2] Sub2    [3] Sub3
mport random, os
from display import boxer
from inventory import Inventory
from pygame import mixer


# Main Initialization #
player = ['']
personalhistory = ''
inv = ''
options = ['[1] Hunt in the Jungle', '.', '.', '.', '.']
costs = [' Cost [20] Stamina', '.', '.', '.', '.',]

actualsituation = 'For some reason, you lost your memory and dont remember anything before Lester wakes you'


class Hostile():
    def __init__(self, name, hp, defense, mindmg, maxdmg):
        self.name = name
        self.hp = hp
        self.maxhp = hp
        self.defense = defense
        self.mindmg = mindmg
        self.maxdmg = maxdmg
        self.id = mobsonroundcount
        self.dodge = 5

class Player():
    def __init__(self, name): 
        self.identity = 0   
        self.name = name
        self.hp = 100
        self.maxhp = self.hp
        self.stamina = 100
        self.maxstamina = self.stamina
        self.level = 1
        self.exp = 0
        self.expnextlevel = 100
        self.strengh = 2
        self.agility = 2
        self.inteligence = 2

def actionmenu():
    hud(0)
    userinput = input(f"{options[0]}{costs[0]} \n{options[1]}{costs[1]} \n{options[2]}{costs[2]} \n{options[3]}{costs[3]} \n{options[4]}{costs[4]} \n\nTerminal: ")
    if chapter == 1:
        if userinput == '1':
            player[0].stamina
            random.randint()
            boxer('You discouver')
  
def sortuple(tup):
    lst = len(actualround)
    for i in range(0, lst):
        for j in range(0, lst-i-1):
            if (actualround[j][1] > actualround[j + 1][1]):
                temptup = actualround[j]
                actualround[j] = actualround[j + 1]
                actualround[j + 1] = temptup
    return f'Actual round in crescent order: {actualround}'

def combat(attacker, target, mode):  # Mode > 2 = Player attack mob  | 1 = Mob attack player
    if mode == 2:
        try:
            intx = player[attacker].skillnum
            inty = 0
            while intx > 0:
                print(player[attacker].skills[inty][0], '[' + str(inty) + ']')
                intx -= 1
                inty += 1
            userinput = input('Choose Action ID: ')
            try:
                input(f"{player[attacker].name} uses {player[attacker].skills[int(userinput)][0]} against {hostilename[target]}")
                trydodge = random.randint(0, 100)
                if trydodge > hostile[target].dodge:
                    damage = player[attacker].skills[int(userinput)][1] - hostile[target].defense
                    if damage > 0:
                        if hostile[target].hp <= damage:    
                            input(f"{hostile[target].name} takes {damage} dmg")
                            input("And, dies.")
                            hostile[target].hp = 0
                            hostilename[target] = hostile[target].name + ' HP:(Dead)'
                            situationmenu()
                        else:
                            input(f"{hostile[target].name} takes {damage} dmg")
                            hostile[target].hp -= damage
                            hostilename[target] = hostile[target].name + ' HP:(' + str(hostile[target].hp) + '/' + str(hostile[target].maxhp) + ')' + ' ID:[' + str(hostile[target].id) + ']'
                            input(hostilename[target])
                            situationmenu()
                    else:
                        input(f"{hostile[target].name} block the attack")
                        situationmenu()
                else:
                    input(f"{hostile[target].name} dodges the attack")
                    situationmenu()
            except ValueError:
                input('Error, incorrect value')
                situationmenu()
        except IndexError:
            input('Error, skill not found')
            situationmenu()
    elif mode == 1:
        try:
            playername = player[target].name + ' HP:(' + str(player[target].hp) + '/' + str(player[target].maxhp) + ')'
            hostilename[attacker] = hostile[attacker].name + ' HP:(' + str(hostile[attacker].hp) + '/' + str(hostile[attacker].maxhp) + ')' + ' ID:[' + str(hostile[attacker].id) + ']'
            input(f"{hostilename[attacker]} try to attack {playername}")
            trydodge = random.randint(0, 100)
            if trydodge > int(player[target].agility):
                #playerdefense = int(player[target].agility) / 2
                damage = random.randint(hostile[attacker].mindmg, hostile[attacker].maxdmg)
                if damage > 0:
                    if player[target].hp <= damage:
                        input(f"{playername} takes {damage} dmg")
                        input("And, dies.")
                        player[target].hp = 0
                        playername = player[target].name + ' HP:(Dead)'
                        situationmenu()
                    else:
                        input(f"{playername} takes {damage} dmg")
                        player[target].hp -= damage
                        playername = player[target].name + ' HP:(' + str(player[target].hp) + '/' + str(player[target].maxhp) + ')'
                        input(playername)
                        situationmenu()
                else:
                    input(f"{player[target].name} block the attack")
                    situationmenu()
            else:
                input(f"{player[target].name} dodges the attack")
                situationmenu()
        except IndexError:
            input('Error, hostile not found')
            situationmenu()
##################################################################


def createplayer(name):
    clear()
    player = Player(name)
    input('You have 10 points to put on attributes')
    points = 15
    while points > 0:
        information = '[' + player.name + '] Strengh: [' + str(player.strengh) + '] Agility: [' + str(player.agility) + '] Inteligence: [' + str(player.inteligence) + ']'
        boxer(information)
        userinput = input('[1] Add Strengh\n[2] Add Agility\n[3] Add Inteligence\n[0] Reset\n\nTerminal: ')
        if userinput == '1':
            player.strengh += 1
            points -= 1
        elif userinput == '2':
            player.agility += 1
            points -= 1
        elif userinput == '3':
            player.inteligence += 1
            points -= 1
        elif userinput == '0':
            userinput = input('Confirm reset?\n[1] Confirm\n[0] Cancel\n\nTerminal: ')
            if userinput == '1':
                player.strengh = 2
                player.agility = 2
                player.inteligence = 2
                points = 15
            else:
                return  ######Set the habilities or attributes that is important on a castaway
        else:
            clear()
            input('Invalid Input!')
    boxer(information)
    userinput = input('Is everything right?\n[1] Confirm\n[0] Reset\n\nTerminal: ')
    if userinput == '0':
        player.strengh = 2
        player.agility = 2
        player.inteligence = 2
        points = 15
        createplayer(player.name)
    else:
        clear()


def takeaction(actualsituation):
    boxer(actualsituation)
    userinput = 'a'

def clear():
    os.system('clear' if os.name=='nt' else 'clear')

def hud(playerid):
    playershowclass = ' Lv ' + str(player[playerid].level) + ' [' + str(player[playerid].exp) + '/' + str(player[playerid].expnextlevel) + '] '
    playershowpoints = '  ' + str(player[playerid].hp) + '/' + str(player[playerid].maxhp) + '   ' + str(player[playerid].stamina) + '/' + str(player[playerid].maxstamina)
    playerstatus = '     | ' + player[playerid].name + (' ' * (14 - len(player[playerid].name))) + '| ' + playershowclass + (' ' * (24 - len(playershowclass))) + '|' + playershowpoints + (' ' * (18 - len(playershowpoints))) + '  | '
    hudplayer = '      | Player       | Class                   |    HP    | Stamina  | Location                   \n ' + playerstatus
    hudfinal = (hudplayer + (' ' * (209 - len(hudplayer))))
    boxer(hudfinal)

def playermenu():
    global musicstate
    mixer.Sound.play(clicksound)
    userinput = input(f'[1] Take a Action\n[2] Open Inventory\n[3] ...\n[4] Options\n\nTerminal: ')
    if userinput == '2':
        mixer.Sound.play(clicksound)
        clear()
        inv.draw()
        input("\n" + ('#' * 100) + "\n\nTerminal: ")
        mixer.Sound.play(clicksound)
        clear()
        hud(0)
        playermenu()
    elif userinput == '4':
        mixer.Sound.play(clicksound)
        boxer(("[1] Music is " + musicstate + "\n[0] Back"))
        userinput = input('\n\nTerminal: ')
        mixer.Sound.play(clicksound)
        if userinput == '1':
            if mixer.music.get_volume() > 0: 
                musicstate = '[ OFF ]'
                mixer.music.set_volume(0)
                clear()
                hud(0)
                playermenu()
            else:
                musicstate = '[ ON ]'
                mixer.music.set_volume(1)
                clear()
                hud(0)
                playermenu()
        else:
            clear()
            hud(0)
            playermenu()
    

################################    Game Start \/
mixer.init()
mixer.music.load('sounds/playermenu.wav')
clicksound = mixer.Sound('sounds/click.wav')
musicstate = '[ ON ]'


userinput = input('\nEnter your name: ')
while len(userinput) < 4 or len(userinput) > 14 or userinput.isdigit():
    mixer.Sound.play(clicksound)
    input('Error! Must be at least 4 caracter and max 14 caracter')
    clear()
    userinput = input('Enter your name: ')

createplayer(str(userinput))

mixer.Sound.play(clicksound)
history = '[Lester]: Alright, ' + str(userinput) + '. Be careful, they still here somewere. We have to get out of here. I will  search for survivors in another place, see you around.'
boxer(history)
input('\n\nPress enter do Continue')
mixer.Sound.play(clicksound)
allplayerscount = 1
player[0] = Player(str(userinput))
inv = Inventory(2)
personalhistory = '[' + player[0].name + ']: Agh! What is happening? I cant remember anything and my head keep spinning. Who is Lester? And where am i? '
boxer(personalhistory)
input('\n\nPress enter do Continue')
mixer.Sound.play(clicksound)
clear()
mixer.music.play(-1)
musicstate = '[ ON ]'
hud(0)
playermenu()
    
                

