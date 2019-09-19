import os

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
        
        hud(0)
    else:
        input('Error, max 14 caracter')
        createplayer(playerid)




createplayer(0)
hud(0)
