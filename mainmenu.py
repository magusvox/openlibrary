import os
from display import boxer
from pygame import mixer

#pygame.init()
#atmosphere = pygame.mixer.Sound("mainmenu.strange-stuff.ogg")

def platform():
    boxer('                     Terminal Role Play   By: MagusVOX ')
    userinput = input('[1] Start a New Game\n[2] Load Game (Not Available)\n[3] Options(Not Available)\n[0] Exit\n\nTerminal: ')
    mixer.Sound.play(clicksound)
    if userinput == '1':
        mixer.Sound.play(clicksound)
        boxer('                     Start a New Game')
        userinput = input('[1] Single Player\n[2] Multi-Player (Not Available)\n[0] Back to menu\n\nTerminal: ')
        if userinput == '1':
            mixer.Sound.play(clicksound)
            boxer('Terminal Role Play is a experiment. The main goal is to make a game all on text that can run on any pc by terminal. Feel free to modify and send pull requests on Github. ')
            input('\n\nPress Enter to Continue ')
            mixer.Sound.play(clicksound)
            boxer('[Strange]: Wake up, Mr... dont know your name, but now you are a free man! lets get out of this     place, its not safe here. ')
            input('\n\nPress Enter to Continue ')
            mixer.Sound.play(clicksound)
            boxer('[Lester]: By the way, my name is Lester, what is your name? ')
            input('\n\nPress Enter to Continue ')
            mixer.Sound.play(clicksound)
            import rpg
        else:
            mixer.Sound.play(clicksound)
            platform()
    elif userinput == '0':
        mixer.Sound.play(clicksound)
        userinput = input('Are you sure? [Y] to confirm ')
        if userinput.upper() == 'Y':
            exit()
        else:
            mixer.Sound.play(clicksound)
            platform()
    else:
        input("Error: invalid input [98]")
        platform()

def clear():
    os.system('clear' if os.name=='nt' else 'clear')



clear()
clear()
mixer.init()
mixer.music.load('sounds/mainmenu.strange-stuff.ogg')
clicksound = mixer.Sound('sounds/click.wav')
mixer.music.play(-1)
print(f"{'#' * 100}\nPress Enter to Continue!\n{'#' * 100}\n\n")
input('')
platform()