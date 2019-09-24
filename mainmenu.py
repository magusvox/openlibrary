import os
from display import boxer

def platform():
    title = ' Terminal Role Play   By: MagusVOX'
    boxer(title, 1)
    userinput = input('[1] Start a New Game\n[2] Load Game (Not Available)\n[3] Options(Not Available)\n[0] Exit\n\nTerminal: ')
    if userinput == '1':
        clear()
        title = ' Start a New Game '
        boxer(title, 1)
        userinput = input('[1] Single Player\n[2] Multi-Player (Not Available)\n[0] Back to menu\n\nTerminal: ')
        if userinput == '1':
            clear()
            history = ' Terminal Role Play is a experiment. The main goal is to make a game all on text that can run on any pc by terminal. Feel free to modify and send pull requests on Github. '
            boxer(history, 2)
            input('\n\nPress Enter to Continue ')
            clear()
            print('#' * 110)
            history = ' [Strange]: Wake up, Mr... dont know your name, but now you are a free man! lets get out of this place,   its not safe here. '
            boxer(history, 2)
            input('')
            clear()
            print('#' * 110)
            history = ' [Lester]: By the way, my name is Lester, what is your name? '
            boxer(history, 2)
            input('')
            clear()
            import rpg
        else:
            input('w')
            clear()
            platform()
    elif userinput == '0':
        userinput = input('Are you sure? [Y] to confirm ')
        if userinput.upper() == 'Y':
            exit()
        else:
            input('w')
            platform()
    else:
        input("Error: invalid input [98]")
        platform()

def clear():
    os.system('clear' if os.name=='nt' else 'clear')


clear()
platform()