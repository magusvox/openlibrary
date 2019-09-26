import os

useroptions = ['Look Around', 'Jump', 'Menu']

def clear():
    os.system('clear' if os.name=='nt' else 'clear')

def playeroptions(options):
    haschoose = False
    while haschoose == False:
        clear()
        count = 1
        for option in options:
            print('[' + str(count) + '] ' + option)
            count += 1
        userinput = input('\n\nTerminal: ')
        if int(userinput) >= 0 and int(userinput) < count:
            return userinput
        


print(playeroptions(useroptions))