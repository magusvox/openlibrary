class Inventory:
    def __init__(self, size):
        self.size = size
        self.maxsize = self.size * self.size
        self.items = []
        self.numitem = 0

    def collect(self, item):
        if (self.numitem + 1) < self.maxsize:
            x = self.numitem + 1
            y = self.numitem + 1
            self.items.insert(self.numitem, (str(item), x, y))
            print(self.numitem)
            self.numitem += 1   #continue here (troubleshot: after add numitem +1 the second item has to appers on (2, 2) but its not
        else:
            print('no enough space')

    def show(self):
        columns = self.size
        rows = self.size
        slot = []
        x = self.numitem + 1     # Quantity of items
        z = 0                   # Items progression
        while columns > 0:
            while rows > 0:
                controw = self.size
                y = 0           # Slot progression
                while controw > 0:
                    if x > 0:
                        try:
                            if columns == self.items[z][2] and rows == self.items[z][1]:
                                inv = self.items[z][0] + (' ' * (10 - len(self.items[z][0])))
                                slot.insert(y, inv)
                                rows -= 1
                                controw -= 1
                                y += 1
                                x -= 1
                                z += 1
                            else:
                                inv = '##########'
                                slot.insert(y, inv)
                                y += 1
                                rows -= 1
                                controw -= 1
                        except IndexError:
                            return
                    else:
                        inv = '##########'
                        slot.insert(y, inv)
                        y += 1
                        rows -= 1
                        controw -= 1
            print(slot)
            slot = []
            columns -= 1
            rows = self.size

inv = Inventory(3)
#inv.items.insert(0, ('Sword +3', 2, 2))
#inv.items.insert(1, ('Shield +2', 1, 1))
#inv2 = Inventory(4)
inv.collect('testt')
print(inv.show())
inv.collect('test2')


print(inv.show())
#print(inv2.show())
