import os
player = []
def boxer(texting, mode):  # 0 = text   |   1 = Centralized and closed scope    |   2 = bottom scope open
    textsize = len(texting)
    line = ['','','','','','','','','','']  # max 10 lines
    start = 0
    end = 106
    page = 0
    line[page] = '# ' + texting[start:end] + (' ' * (96 - len(texting))) + ' #'
    while textsize > 96 and mode == 0:
        line[page] = '# ' + texting[start:end] + (' ' * (95 - len(texting))) + ' #'
        print(line[page])
        start += 106
        end += 106
        page += 1
        textsize -= 96
    if textsize > 0 and textsize < 96 and mode == 0:
        line[page] = '# ' + texting[start:(start + textsize)] + (' ' * (96 - textsize)) + ' #'
        print(line[page])
        textsize = 0
    if textsize > 0 and textsize < 96 and mode == 1:
        print('#' * 110)
        line[page] = ('#' + (' ' * 35) + texting + (' ' * (73 - textsize)) + '#')
        print(line[page])
    while textsize > 106 and mode == 2:
        line[page] = '# ' + texting[start:end] + (' ' * (106 - len(texting))) + ' #'
        print(line[page])
        start += 106
        end += 106
        page += 1
        textsize -= 106
    if textsize > 0 and textsize < 106 and mode == 2:
        line[page] = '# ' + texting[start:(start + textsize)] + (' ' * (106 - textsize)) + ' #'
        print(line[page])
        textsize = 0
        print('#' * 110)
        return
    print('#' * 110)

def hud(playerid):
    clear()
    playershowclass = player[playerid].race + ' Lv ' + str(player[playerid].level) + ' [' + str(player[playerid].exp) + '/' + str(player[playerid].expnextlevel) + '] '
    playershowpoints = '  ' + str(player[playerid].hp) + '/' + str(player[playerid].maxhp) + '    ' + str(player[playerid].mana) + '/' + str(player[playerid].maxmana) + '   ' + str(player[playerid].stamina) + '/' + str(player[playerid].maxstamina)
    playerstatus[playerid] = '     | ' + player[playerid].name + (' ' * (14 - len(player[playerid].name))) + '| ' + playershowclass + (' ' * (24 - len(playershowclass))) + '|' + playershowpoints + (' ' * (30 - len(playershowpoints))) + '  | ' + player[playerid].location
    hudplayer[playerid] = '      | Player[' + str(player[playerid].identity) + ']     | Class                   |    HP    |   Mana   | Stamina  | Location                 #\n# ' + playerstatus[playerid]
    hudfinal = ('#' + hudplayer[playerid] + (' ' * (219 - len(hudplayer[playerid]))) + '#\n' + ('#' * 110))
    print(hudfinal)
    

def clear():
    os.system('cls' if os.name=='nt' else 'clear')