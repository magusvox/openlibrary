def inventory(intx, inty):
    columns = 3
    rows = 3
    x = 3
    slot = []
    while columns > 0:
        while rows > 0:
            controw = x
            y = 0
            while controw > 0:
                if rows == intx and columns == inty:
                    inv = '   Item   '
                    slot.insert(y, inv)
                    y += 1
                    rows -= 1
                    #inv = (columns, rows)
                    inv = '##########'
                    controw -= 1
                else:
                    #inv = (columns, rows)
                    inv = '##########'
                    slot.insert(y, inv)
                    y += 1
                    rows -= 1
                    controw -= 1
        print(slot)
        slot = []
        columns -= 1
        rows = x

inventory(2, 2)