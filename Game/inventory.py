class Item(object):

    def __init__(self, name, points, damage, amount, key):
        self.name = name
        self.points = points
        self.damage = damage
        self.amount = amount
        self.key = key

class Inventory(object):

    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item.name] = item

    def print_items(self):
        print('\t'.join(['Name', 'Points', 'Damage', 'Amount', 'Key']))
        for item in self.items.values():
            print('\t'.join([str(x) for x in [item.name, item.points, item.damage, item.amount, item.key]]))

inventory = Inventory()
inventory.add_item(Item('grass', 1, 0, 20, 11))
inventory.add_item(Item('flowers', 2, 0, 10, 12))
inventory.add_item(Item('tree', 4, 0, 5, 13))
inventory.add_item(Item('hoe', 0, 1, 1, 14))
inventory.print_items()
