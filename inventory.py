def inventory(intx, inty):
    columns = 5
    rows = 5
    x = 5
    line = []
    allslots = columns * 1
    inv = (columns, rows)
    while columns > 0:
        while rows > 0:
            if inv == (intx, inty):
                inv = (0, 0)
                line += inv
                rows -= 1
                inv = (columns, rows)
            else:
                line += inv
                rows -= 1
                inv = (columns, rows)
        print(line)
        line = []
        columns -= 1
        rows = x
        inv = (columns, rows)

inventory(3, 3)

