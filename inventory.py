class Inventory:
    def __init__(self, size):
        self.size = size
        self.slots = self.size * self.size
        self.items = []
        self.slotx = self.size
        self.sloty = self.size
        self.itemson = 0

    def collect(self, item):
        if self.itemson < self.slots:
            self.items.insert(self.itemson, (('[' + str(self.itemson + 1)+ '] ' + str(item)), self.slotx, self.sloty))
            self.itemson += 1
            if self.slotx == 1:
                self.slotx = self.size
                self.sloty -= 1
            else:
                self.slotx -= 1
        else:
            return

    def drop(self, itemid):
        if itemid <= self.itemson:
            self.items.insert(itemid, '##########')  # continuehere
        else:
            print('q')

    def draw(self):
        columns = self.size
        rows = self.size
        slot = []
        x = self.itemson     # Quantity of items
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
        return f"Inventory capacity: [{self.itemson}/{self.slots}]"

inv = Inventory(3)
inv.collect('sword')
inv.collect('knife')

inv.collect('helmet')
inv.collect('rock')
inv.collect('sword')
inv.collect('helmet')
inv.collect('rock')
inv.collect('final')



input(inv.draw())
input(inv.drop(3))
input(inv.draw())
