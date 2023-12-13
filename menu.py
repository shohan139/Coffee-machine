class MenuItem:
    # Models each Menu Item
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

class Menu:
    # Models the Menu with drinks
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", cost = 2.5),
            MenuItem(name="espresso", cost = 1.5),
            MenuItem(name="cappuccino", cost = 3), # coffee recipe in grams
        ]
    
    def set_items(self, item):
        if item==1:
            return "espresso"
        elif item==2:
            return "latte"
        else:
            return "cappuccino"

    def get_items(self):
        # Returns all the names of the available menu items
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options
    
    def find_drink(self, order_name):
        # Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")
        return 0
        
