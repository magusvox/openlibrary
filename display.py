import os
player = []
def boxer(text):
    clear()
    print(f"\n{text}\n\n{'#' * 70}")

def hud(playerid):
    clear()
    playershowclass = player[playerid].race + ' Lv ' + str(player[playerid].level) + ' [' + str(player[playerid].exp) + '/' + str(player[playerid].expnextlevel) + '] '
    playershowpoints = '  ' + str(player[playerid].hp) + '/' + str(player[playerid].maxhp) + '    ' + str(player[playerid].mana) + '/' + str(player[playerid].maxmana) + '   ' + str(player[playerid].stamina) + '/' + str(player[playerid].maxstamina)
    playerstatus[playerid] = '     | ' + player[playerid].name + (' ' * (14 - len(player[playerid].name))) + '| ' + playershowclass + (' ' * (24 - len(playershowclass))) + '|' + playershowpoints + (' ' * (30 - len(playershowpoints))) + '  | ' + player[playerid].location
    hudplayer[playerid] = '      | Player[' + str(player[playerid].identity) + ']     | Class                   |    HP    |   Mana   | Stamina  | Location       #\n# ' + playerstatus[playerid]
    hudfinal = (hudplayer[playerid] + (' ' * (200 - len(hudplayer[playerid]))) + '\n' + ('#' * 100))
    print(hudfinal)
    

def clear():
    os.system('clear' if os.name=='nt' else 'clear')
