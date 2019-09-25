usrx, usry = 2, 2
roomspace = 4
def walk(x, y, room):
    global usrx, usry
    up, down, left, right = 'Blocked', 'Blocked', 'Blocked', 'Blocked'
    if x > 0:
        left = 'Left'
    if x < room:
        right = 'Right'
    if y > 0:
        down = 'Down'
    if y < room:
        up = 'Up'
    userinput = input(f'Which direction do you wanna walk?\n[1] {up}\n[2] {down}\n[3] {left}\n[4] {right}\n\nTerminal: ')
    if userinput == '1':
        if up != 'Up':
            input('Blocked!')
            y -= 1
            walk(usrx, usry, roomspace)
        else:
            y += 1
    elif userinput == '2':
        if down != 'Down':
            input('Blocked!')
            y += 1
            walk(usrx, usry, roomspace)
        else:
            y -= 1
    elif userinput == '3':
        if left != 'Left':
            input('Blocked!')
            x += 1
            walk(usrx, usry, roomspace)
        else:
            x -= 1
    elif userinput == '4':
        if right != 'Right':
            input('Blocked!')
            x -= 1
            walk(usrx, usry, roomspace)
        else:
            x += 1
    usrx, usry = x, y
    print(usrx, usry)
    return
    
    

while True:
    walk(usrx, usry, roomspace)
    
