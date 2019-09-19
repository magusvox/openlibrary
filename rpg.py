# Missions:
# [0] Main Mission  [1] Sub1    [2] Sub2    [3] Sub3
import random, os
from display import boxer, hud


# Main Initialization #

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

class Player():
    def __init__(self, name, race, strength, agility, constitution, inteligence, carism):
        self.name = name
        self.race = race
        self.strength = strength
        self.agility = agility
        self.constitution = constitution
        self.inteligence = inteligence
        self.carism = carism
        self.level = 1
        self.id = allplayerscount
        self.xp = 0
        self.xpnextlevel = 100
        self.hp = (int(constitution) * 2) + 3
        self.maxhp = (int(constitution) * 2) + 3
        self.skills = [('Simple Attack', 5), ('Fireball', 8)]
        self.skillnum = 2
    def info(self):
        return f'{self.name} is a {self.race} Lv{self.level} ({self.xp}/{self.xpnextlevel})  HP: ({self.hp}/{self.maxhp})\nStr: {self.strength}|Agi: {self.agility}|Con: {self.constitution}|Int: {self.inteligence}|Car: {self.carism}'

def godmenu():
    clear()
    global player
    title = 'God Tools'
    print(f"{'#' * 10} {title} {'#' * (40 - len(title))}")
    userinput = input(f"[1] Add mission\n[2] Modify Player status\n[4] empty\n[5] Back to tools\nChoose a option: ")
    if userinput == '1':
        godmenu()
    elif userinput == '2':
        userinput = input("Enter player ID: ")
        playerid = int(userinput)
        try:
            print(f'Actual Str of {player[playerid].name}: {player[playerid].strength}')
            userinput = input('New Strength: ')
            player[playerid].strength = int(userinput)
            print(f'Actual Agi of {player[playerid].name}: {player[playerid].agility}')
            userinput = input('New Agility: ')
            player[playerid].agility = int(userinput)
            print(f'Actual Con of {player[playerid].name}: {player[playerid].constitution}')
            userinput = input('New Constitution: ')
            player[playerid].constitution = int(userinput)
            player[playerid].hp = (player[playerid].constitution * 2) + 3
            player[playerid].maxhp = (player[playerid].constitution * 2) + 3
            print(f'Actual Int of {player[playerid].name}: {player[playerid].inteligence}')
            userinput = input('New Inteligence: ')
            player[playerid].inteligence = int(userinput)
            print(f'Actual Car of {player[playerid].name}: {player[playerid].carism}')
            userinput = input('New Carism: ')
            player[playerid].carism = int(userinput)
            print(f'Actual Lvl of {player[playerid].name}: {player[playerid].level}')
            userinput = input('New Level: ')
            player[playerid].level = int(userinput)
            input(f'Successful!\n{player[playerid].info()}')
            godmenu()
        except IndexError:
            input("Player not found.")
            godmenu()
    elif userinput == '5':
        tools()
    else:
        input("invalid input [155]")
        godmenu()

def createplayer(name):
    clear()
    global player, allplayers, allplayerscount
    createdplayer = Player(name, input("Race: "), input("Strenght: "), input("Agility: "), input("Constitution: "), input("Inteligence: "), input("Carism: "))
    allplayers.insert(allplayerscount, ('Player:', allplayerscount, "Name:" + createdplayer.name, "ID:", allplayerscount))
    player.insert((allplayerscount + 1), '')
    player[allplayerscount] = createdplayer
    allplayerscount += 1
    input(f"Succesful! {createdplayer.name} is the Player N:{createdplayer.id}")
    menu()

def playersmenu():
    clear()
    title = 'Players Menu'
    print(f"{'#' * 10} {title} {'#' * (40 - len(title))}")
    userinput = input('[1] Create new Player\n[2] Player stats\n[3] nsei\n[4] nsei\n[5] Back to menu\nChoose a option: ')
    if userinput == '1':
        createplayer()
    elif userinput == '2':
        userinput = input('Enter player ID: ')
        try:
            input(player[int(userinput)].info())
            playersmenu()
        except IndexError:
            input("Player not found")
            playersmenu()
    elif userinput == '5':
        clear()
        menu()
    else:
        input('Invalid Input [188]')
        playersmenu()

def roundmanager():
    clear()
    global actualround, mobsituationlist, mobsonroundcount, hostile
    title = 'Round Manager'
    print(f"{'#' * 10} {title} {'#' * (30 - len(title))} {str(mobsonroundcount)}")
    userinput = input('[1] Hostile Situation\n[2] empty\n[3] empty\n[4] empty\n[5] Back to menu\nChoose a option: ')
    if userinput == '1':
        clear()
        situationmenu()
    elif userinput == '2':
        situationmenu()
    elif userinput == '3':
        clear()
        roundmanager()
    elif userinput == '4':
        roundmanager()     
    elif userinput == '5':
        clear()
        menu()
    else:
        input('Invalid Input [211]')
        roundmanager()

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

def tools():
    clear()
    title = 'Tools'
    print(f"{'#' * 10} {title} {'#' * (40 - len(title))}")
    userinput = input('[1] Dices\n[2] Round Manager\n[3] Player def\n[4] God tools\n[5] Back to menu\nChoose a option: ')
    if userinput == '1':
        userinput = input('[1] D4\n[2] D6\n[3] D8\n[4] D10\n[5] D20\n[0] custom\nChoose: ')
        if userinput == '1':
            input(f'The dice D4 rolls... {random.randint(1, 4)}')
            tools()
        elif userinput == '2':
            input(f'The dice D6 rolls... {random.randint(1, 6)}')
            tools()
        elif userinput == '3':
            input(f'The dice D8 rolls... {random.randint(1, 8)}')
            tools()
        elif userinput == '4':
            input(f'The dice D10 rolls... {random.randint(1, 10)}')
            tools()
        elif userinput == '5':
            input(f'The dice D20 rolls... {random.randint(1, 20)}')
            tools()
        elif userinput == '0':
            intx = input('Enter custom dice max result: ')
            try:
                input(f'The dice D{intx} rolls... {random.randint(1, int(intx))}')
                tools()
            except ValueError:
                input('oops')
                tools()
        else:
            input('Invalid input [476]')
            tools()
    elif userinput == '2':
        roundmanager()
    elif userinput == '3':
        userinput = input('player id: ')
        #input(defense(int(userinput)))
        tools()
    elif userinput == '4':
        godmenu()
    elif userinput == '5':
        clear()
        menu()
    else:
        input('Invalid input [490]')
        clear()
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
    os.system('cls' if os.name=='nt' else 'clear')


userinput = input('\n\nEnter your name: ')
if len(userinput) < 4 or len(userinput) > 14 or userinput.isdigit():
    input('Error! Must be at least 4 caracter and max 14 caracter')
    clear()
    userinput = input('Enter your name: ')
else:
    clear()
    print('#' * 110)
    history = ' [Lester]: Alright, ' + str(userinput) + '. I will search for survivors in another place, see you around.'
    boxer(history, 2)
    createplayer(str(userinput))
                

