# Missions:
# [0] Main Mission  [1] Sub1    [2] Sub2    [3] Sub3
import random, os
from display import boxer
from inventory import Inventory


# Main Initialization #
player = ['']
personalhistory = ''
inv = ''
mobsituationlist = []
mobsonround = []
mobsonroundcount = 0
mobsonroundcount2 = 0  # This var is for showing hostilenames even when a mob dies and the mobsonroundcunt is subtracted to -1
actualround = ['']
hostile = []
hostilename = []
mobsdeadcount = 0
randomnpc = ['Hunter', 'Wise man', 'Citizen', ]
easymobs = ['Wolf', 'Boar', 'Goblin', 'Little Bear']
easyitems = ['Short sword(+2)', 'Rope', 'trash', 'Animal skin', '5 Coins']
mediummobs = ['Bandit', 'Goblin', 'Ranged Goblin', 'Bear', 'Wolf']
mediumitems = ['Armor(+3)', 'Potion(+5)', 'Sword(+4)', '10 Coins', '15 Coins', '5 Coins']
hardmobs = ['Stormclock soudier']
moblevel = 0

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
class Entity:
    hp = 100
    maxhp = hp
    stamina = 100
    maxstamina = stamina
    mana = 100
    maxmana = mana
    race = 'Human'
    humor = 0
    typeof = 0  # 0 = Player | 1 = Friendly | 2 = Hostile
    location = 'Unknown'
    def interact(self, other):  # other = get id
        print(f"{self.name} interacts with {other.name}")

class Player(Entity):
    def __init__(self, name): 
        self.identity = 0   
        self.name = name
        self.level = 1
        self.exp = 0
        self.expnextlevel = 100
        self.strengh = 0
        self.agility = 0
        self.inteligence = 0

def situationmenu():
    clear()
    global mobsituationlist, mobsonroundcount, mobsonroundcount2, moblevel, hostile, easyitems, actualround, hostilename, mobsdeadcount
    title = 'Situation Generator'
    print(f"{'#' * 10} {title} {'#' * (30 - len(title))} Actual round: {actualround}")
    ##### Pre-initializations, this can be on a single function on future, but for now
    ##### it will be here some codes that has to be run to show the actual stats
    if mobsonroundcount > 0:  # Mobs name/hp
        inty = mobsonroundcount2
        intx = 0
        mobsituationlist = []    
        while inty > 0:
            mobsituationlist.insert(intx, hostilename[intx])
            inty -= 1
            intx += 1
    else:
        mobsonroundcount2 = 0
    tempplayerslist = allplayerscount
    intx = 0
    allplayers = []
    while tempplayerslist > 0:
        allplayers.insert(intx, player[intx].name + ' HP:(' + str(player[intx].hp) + '/' + str(player[intx].maxhp) + ') ID:[' + str(player[intx].id) + ']')
        tempplayerslist -= 1
        intx -= 1
    userinput = input(f'[1] Generate a Mob Encounter\n[2] Generate Round Order\n[3] Get Attacked by Mob > {allplayers}\n[4] Attack/Interact with > {mobsituationlist}\n[5] Back to Round manager\nChoose a option: ')
    if userinput == '1':
        if mobsonroundcount == 0:
            userinput = input('Dificulty level: ')
            try:
                moblevel = int(userinput)  # Level of mobs
                inty = random.randint((allplayerscount - (random.randint(0, allplayerscount))), allplayerscount)  # Quantity of mobs
                intyground = 0
                # inty = Random int between ALL - (rand 0, all) and ALL
                mobsituationtemp = []
                #Easy Mobs creation
                while inty > 0 and moblevel <= 3:
                    mob = random.randint(0, (len(easymobs) - 1))
                    mobsituationtemp.insert(inty, (easymobs[mob]))
                    mobsonroundcount += 1
                    mobsonroundcount2 += 1
                    inty -= 1
                    if 'Wolf' in mobsituationtemp[intyground]:
                        hostile.insert(intyground, Hostile('Wolf', 10, 1, 3, 5))
                        hostilename.insert(intyground, hostile[intyground].name + ' HP:(' + str(hostile[intyground].hp) + '/' + str(hostile[intyground].maxhp) + ') ID:[' + str(intyground) + ']')
                        intyground += 1
                    elif 'Boar' in mobsituationtemp[intyground]:
                        hostile.insert(intyground, Hostile('Boar', 9, 0, 2, 4))
                        hostilename.insert(intyground, hostile[intyground].name + ' HP:(' + str(hostile[intyground].hp) + '/' + str(hostile[intyground].maxhp) + ') ID:[' + str(intyground) + ']')
                        intyground += 1
                    elif 'Goblin' in mobsituationtemp[intyground]:
                        hostile.insert(intyground, Hostile('Goblin', 14, 2, 4, 6))
                        hostilename.insert(intyground, hostile[intyground].name + ' HP:(' + str(hostile[intyground].hp) + '/' + str(hostile[intyground].maxhp) + ') ID:[' + str(intyground) + ']')
                        intyground += 1
                    elif 'Little Bear' in mobsituationtemp[intyground]:
                        hostile.insert(intyground, Hostile('Little Bear', 13, 0, 4, 5))
                        hostilename.insert(intyground, hostile[intyground].name + ' HP:(' + str(hostile[intyground].hp) + '/' + str(hostile[intyground].maxhp) + ') ID:[' + str(intyground) + ']')
                        intyground += 1
                #Medium Mobs creation ['Bandit', 'Goblin', 'Ranged Goblin', 'Bear', 'Wolf']
                while inty > 0 and moblevel > 3 and moblevel <= 6:
                    mob = random.randint(0, (len(mediummobs) - 1))
                    mobsituationtemp.insert(inty, (mediummobs[mob]))
                    if 'Wolf' in mobsituationtemp[intyground]:
                        hostile.insert(intyground, Hostile('Wolf', 10, 1, 3, 5))
                        hostilename.insert(intyground, hostile[intyground].name + ' HP:(' + str(hostile[intyground].hp) + '/' + str(hostile[intyground].maxhp) + ') ID:[' + str(intyground) + ']')
                        intyground += 1
                    elif 'Bandit' in mobsituationtemp[intyground]:
                        hostile.insert(intyground, Hostile('Bandit', 14, 2, 5, 6))
                        hostilename.insert(intyground, hostile[intyground].name + ' HP:(' + str(hostile[intyground].hp) + '/' + str(hostile[intyground].maxhp) + ') ID:[' + str(intyground) + ']')
                        intyground += 1
                    elif 'Goblin' in mobsituationtemp[intyground]:
                        hostile.insert(intyground, Hostile('Goblin', 14, 2, 4, 6))
                        hostilename.insert(intyground, hostile[intyground].name + ' HP:(' + str(hostile[intyground].hp) + '/' + str(hostile[intyground].maxhp) + ') ID:[' + str(intyground) + ']')
                        intyground += 1
                    elif 'Ranged Goblin' in mobsituationtemp[intyground]:
                        hostile.insert(intyground, Hostile('Ranged Goblin', 10, 0, 5, 7))
                        hostilename.insert(intyground, hostile[intyground].name + ' HP:(' + str(hostile[intyground].hp) + '/' + str(hostile[intyground].maxhp) + ') ID:[' + str(intyground) + ']')
                        intyground += 1
                    elif 'Bear' in mobsituationtemp[intyground]:
                        hostile.insert(intyground, Hostile('Bear', 16, 3, 4, 7))
                        hostilename.insert(intyground, hostile[intyground].name + ' HP:(' + str(hostile[intyground].hp) + '/' + str(hostile[intyground].maxhp) + ') ID:[' + str(intyground) + ']')
                        intyground += 1
                    mobsonroundcount += 1
                    mobsonroundcount2 += 1
                    inty -= 1
                mobsituationlist = mobsituationtemp
                input(mobsituationlist)
                situationmenu()
            except ValueError:
                input('Invalid Input [302]')
                situationmenu()
        else:
            input('Already on Hostile Situation, cant create a new one.')
            situationmenu()
    elif userinput == '2':
        try:
            playerturns = allplayerscount
            mobsturns = mobsonroundcount
            turns = allplayerscount + mobsonroundcount
            round = []
            while turns > 0:
                if userinput.upper() != 'EXIT' and playerturns > 0:  # Break loop typing 'exit'
                    userinput = input(f'Extra Attribute for {player[playerturns - 1].name}?: ')
                    result = int(userinput) + random.randint(1, 20)
                    if result > 20:
                        result = 20
                        round.insert(turns, (player[playerturns - 1].name, result))
                        playerturns -= 1
                        turns -= 1
                    else:
                        round.insert(turns, (player[playerturns - 1].name, result))
                        playerturns -= 1
                        turns -= 1
                elif playerturns == 0 and mobsturns > 0:
                    userinput = input(f"Extra Attribute for {hostilename[mobsturns - 1]}: ")  #feels like is almost working, keep on here
                    result = int(userinput) + random.randint(1, 20)
                    if result > 20:
                        result = 20
                        round.insert(turns, (hostilename[mobsturns - 1], result))
                        mobsturns -= 1
                        turns -= 1
                    else:
                        round.insert(turns, (hostilename[mobsturns - 1], result))
                        mobsturns -= 1
                        turns -= 1
                else:
                    input('Canceled')
                    situationmenu()
            actualround = round
            input(sortuple(actualround))
            situationmenu()
        except ValueError:
            input("value error")
            situationmenu()
    elif userinput == '3':
        if mobsonroundcount > 0:
            inty = mobsonroundcount + mobsdeadcount
            intx = 0
            round = []
            while inty > 0:
                print(f'[{intx}] {mobsituationlist[intx]}')
                round.insert(intx, hostilename[intx]) 
                inty -= 1  
                intx += 1 
            try:
                userinput = input('Select the mob: ')
                attacker = int(userinput)
                try:
                    if hostile[attacker].hp <= 0:
                        input('Error, select a mob that is alive')
                        situationmenu()
                    else:
                        print(f'Players: {allplayers}')
                        userinput = input(f'Specify attack of {hostilename[attacker]}?\nEnter player ID or type "random" to randomize\nInput attack target: ')
                        try:
                            if userinput == 'random':
                                target = random.randint(0, allplayerscount - 1)
                                combat(attacker, target, 1)
                            elif userinput.isdigit():
                                target = int(userinput)
                                combat(attacker, target, 1)
                            else:
                                input("Something went whrong")
                                situationmenu()
                        except ValueError:
                            input("Invalid Input [378]")
                            situationmenu()
                except IndexError:
                    input('Invalid Input [381]')
                    situationmenu()
            except ValueError:
                input('Invalid Value')
                situationmenu()
        else:
            input('Error, no mobs on round')
            situationmenu()
    elif userinput == '4':
        userinput = input(f"{allplayers}\nWho will attack?: ")
        try:
            attacker = int(userinput)
            if player[attacker].hp <= 0:
                input(f"{player[attacker].name} cant attack because is dead. Select another player")
                situationmenu()
            else:
                if mobsonroundcount > 0:
                    inty = mobsonroundcount + mobsdeadcount  # Bug solution to show correct moblist after one or more are dead
                    intx = 0
                    round = []
                    while inty > 0:
                        print(f'[{intx}] {mobsituationlist[intx]}')
                        round.insert(intx, hostilename[intx]) 
                        inty -= 1
                        intx += 1
                    userinput = input('Select a target: ')
                    target = int(userinput)
                    print(f"{player[attacker].name} targeted {hostilename[target]}")
                    combat(attacker, target, 2)
                else:
                    input("Something went whrong")
                    situationmenu()
        except IndexError:
            input("Error, Player ID not found.")
            situationmenu()
    elif userinput == '5':
        clear()
        roundmanager()
    else:
        print('Invalid Input[442]')
        situationmenu()
  
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

def clear():
    os.system('clear' if os.name=='nt' else 'clear')

def hud(playerid):
    clear()
    playershowclass = player[playerid].race + ' Lv ' + str(player[playerid].level) + ' [' + str(player[playerid].exp) + '/' + str(player[playerid].expnextlevel) + '] '
    playershowpoints = '  ' + str(player[playerid].hp) + '/' + str(player[playerid].maxhp) + '   ' + str(player[playerid].stamina) + '/' + str(player[playerid].maxstamina)
    playerstatus = '     | ' + player[playerid].name + (' ' * (14 - len(player[playerid].name))) + '| ' + playershowclass + (' ' * (24 - len(playershowclass))) + '|' + playershowpoints + (' ' * (18 - len(playershowpoints))) + '  | ' + player[playerid].location
    hudplayer = '      | Player[' + str(player[playerid].identity) + ']     | Class                   |    HP    | Stamina  | Location                            #\n# ' + playerstatus
    hudfinal = ('#' + hudplayer + (' ' * (219 - len(hudplayer))) + '#\n' + ('#' * 110))
    print(hudfinal)

def playermenu():
    userinput = input(f'[1] Take a Action\n[2] Open Inventory\n[3] ...\n[4] ...\n\nTerminal: ')
    if userinput == '2':
        clear()
        inv.draw()
        input('back')
        clear()
        hud(0)
        playermenu()
    

################################    Game Start \/

userinput = input('\nEnter your name: ')
if len(userinput) < 4 or len(userinput) > 14 or userinput.isdigit():
    input('Error! Must be at least 4 caracter and max 14 caracter')
    clear()
    userinput = input('Enter your name: ')
else:
    clear()
    print('#' * 110)
    history = ' [Lester]: Alright, ' + str(userinput) + '. Be careful, they still here somewere. We have to get out of here. I will search for survivors in another place, see you around.'
    boxer(history, 2)
    input('')
    allplayerscount = 1
    player[0] = Player(str(userinput))
    inv = Inventory(2)
    personalhistory = '[' + player[0].name + ']: Agh! What is happening? I cant remember anything and my head keep spinning. Who is Lester? And where am i? '
    clear()
    boxer(personalhistory, 2)
    input('')
    clear()
    hud(0)
    playermenu()
    
                

