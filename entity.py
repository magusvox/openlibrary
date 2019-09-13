import colorama, os
from colorama import Fore, Style
from mainmenu import boxer


creatorcount = 0
playerstatus = ['', '']
player = []
hudplayer = ['', '']
playerid = ''

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
    location = 'Undefined'
    def interact(self, other):  # other = get id
        print(f"{self.name} interacts with {other.name}")


class Player(Entity):
    def __init__(self, name): 
        self.identity = creatorcount   
        self.name = name
        self.level = 1
        self.exp = 0
        self.expnextlevel = 100
        self.strengh = 0
        self.agility = 0
        self.inteligence = 0

def createplayer(playerid):
    global creatorcount, player
    clear()
    title = ' Creating Player[' + str(playerid) + ']'
    boxer(title, 1)
    userinput = input('Player[' + str(playerid) + '] Name: ')
    if len(userinput) < 15 and len(userinput) > 0:
        player.insert(creatorcount, Player(str(userinput)))
        creatorcount += 1
        
        loop(0)
    else:
        input('Error, max 14 caracter')
        createplayer(playerid)


def loop(playerid):
    clear()
    title = ' Terminal Role Play v0.1 '
    playershowclass = player[playerid].race + ' Lv ' + str(player[playerid].level) + ' [' + str(player[playerid].exp) + '/' + str(player[playerid].expnextlevel) + '] '
    playershowpoints = '  ' + Fore.RED + str(player[playerid].hp) + '/' + str(player[playerid].maxhp) + Style.RESET_ALL + '    ' + Fore.LIGHTBLUE_EX + str(player[playerid].mana) + '/' + str(player[playerid].maxmana) + Style.RESET_ALL + '   ' + Fore.LIGHTYELLOW_EX + str(player[playerid].stamina) + '/' + str(player[playerid].maxstamina) + Style.RESET_ALL
    playerstatus[playerid] = '     | ' + player[playerid].name + (' ' * (14 - len(player[playerid].name))) + '| ' + playershowclass + (' ' * (24 - len(playershowclass))) + '|' + playershowpoints + (' ' * (32 - len(playershowpoints))) + '  | ' + player[playerid].location
    hudplayer[playerid] = '      | Player[' + str(player[playerid].identity) + ']     | Class                   |    HP    |   Mana   | Stamina  | Location       #\n# ' + playerstatus[playerid]
    hudfinal = ('#' * 30) + title + ('#' * (70 - len(title))) + '\n#' + hudplayer[playerid] + (' ' * (226 - len(hudplayer[playerid]))) + '#\n' + ('#' * 100)
    print(hudfinal)
    

def clear():
    os.system('cls' if os.name=='nt' else 'clear')


createplayer(0)
#loop(0)
