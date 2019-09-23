class Inventory:
    def __init__(self, size):
        self.size = size
        self.slots = self.size * self.size
        self.itemslist = []
        self.itemson = 0
        x = self.slots
        while x > 0:
            self.itemslist.insert(x, '[###################')
            x -= 1

    def collect(self, item):
        if self.itemson < self.slots:
            sorting = True
            y = 0   
            while sorting:
                if self.itemslist[y] == '[###################':
                    self.itemslist[y] = ('[' + str(y) + '] ' + str(item))
                    self.itemson += 1
                    sorting = False
                else:
                    y += 1
        else:
            print('No Enough Space')

    def drop(self, itemid):
        if self.itemslist[itemid] != '[###################':
            self.itemslist[itemid] = '[###################'
            self.itemson -= 1
        else:
            print('Slot already free')

    def draw(self):
        print('---------------------')
        x = len(self.itemslist)
        z = 0           # Item print progression
        slotado = 0     # Num of real items
        while x > 0:
            slot = self.itemslist[z] + (' ' * (20 - len(self.itemslist[z])) + ']')
            print(slot)
            x -= 1
            z += 1
            if slot != '[###################]':
                slotado += 1
        print('---------------------')
        return f"Inventory capacity: [{slotado}/{self.slots}]"

inv = Inventory(2)
inv.collect('test')
inv.collect('test2')
print(inv.draw())
inv.drop(0)
print(inv.draw())
inv.collect('test3')
inv.collect('test4')
print(inv.draw())
