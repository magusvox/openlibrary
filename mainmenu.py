import os

def boxer(texting, mode):  # 0 = text   |   1 = Centralized and closed scope    |   2 = bottom scope open
    textsize = len(texting)
    line = ['','','','','','','','','','']  # max 10 lines
    start = 0
    end = 96
    page = 0
    line[page] = '# ' + texting[start:end] + (' ' * (96 - len(texting))) + ' #'
    while textsize > 96 and mode == 0:
        line[page] = '# ' + texting[start:end] + (' ' * (95 - len(texting))) + ' #'
        print(line[page])
        start += 96
        end += 96
        page += 1
        textsize -= 96
    if textsize > 0 and textsize < 96 and mode == 0:
        line[page] = '# ' + texting[start:(start + textsize)] + (' ' * (96 - textsize)) + ' #'
        print(line[page])
        textsize = 0
    if textsize > 0 and textsize < 96 and mode == 1:
        print('#' * 100)
        line[page] = '#                 ' + texting + (' ' * (80 - textsize)) + ' #'
        print(line[page])
    while textsize > 96 and mode == 2:
        line[page] = '# ' + texting[start:end] + (' ' * (95 - len(texting))) + ' #'
        input(line[page])
        start += 96
        end += 96
        page += 1
        textsize -= 96
    if textsize > 0 and textsize < 96 and mode == 2:
        line[page] = '# ' + texting[start:(start + textsize)] + (' ' * (96 - textsize)) + ' #'
        input(line[page])
        textsize = 0
        return
    print('#' * 100)

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def platform():
    clear()
    title = ' Terminal Role Play ALPHA    By: MagusVOX'
    boxer(title, 1)
    userinput = input('[1] Start a New Game\n[2] Load Game\n[3] Options\n[0] Exit\n\nTerminal: ')
    if userinput == '1':
        clear()
        title = ' Start a New Game '
        boxer(title, 1)
        userinput = input('[1] Single Player\n[2] Multi-Player\n[0] Back to menu\n\nTerminal: ')
        if userinput == '1':
            history = ' Terminal Role Play é um RPG medieval de texto, o intuito é criar uma imersão imaginatória onde o jogador se imagina no cenário apresentado textualmente'
            clear()
            print('#' * 100)
            boxer(history, 2)
            import entity
        else:
            platform()
    elif userinput == '2':
        playersplatform()
    elif userinput == '3':
        roundmanager()
    elif userinput == '4':
        tools()
    elif userinput == '0':
        userinput = input('Are you sure? [Y] to confirm ')
        if userinput.upper() == 'Y':
            exit()
        else:
            platform()
    else:
        input("Error: invalid input [98]")
        platform()