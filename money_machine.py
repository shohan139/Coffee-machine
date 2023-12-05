class MoneyMachine:
    CURRENCY = "$"

    def __init__(self):
        # TODO: we should return this profit somewhere in the code, otherwise it's useless.
        self.profit = 0
        self.money_received = 0

    def report(self):
        # Prints the current profit
        print(f"Money: {self.CURRENCY}{self.profit}")
    
    def process_coins(self):
        # Returns the total calculated from inserted

        while True:
            try:
                self.money_received = float(input('''\033[33m
            Enter your money: \033[m
            '''))
            except:
                if type(self.money_received) != "float":
                    print("Wrong input! Try again")
            else:
                if self.money_received<=0:
                    print("Wrong input! Try again")
                else:
                    break
        return self.money_received
    
    def make_payment(self, cost):
        # Return True when payment is accepted, False if insufficient
        self.process_coins()
        if self.money_received >= cost:
            self.change = round(self.money_received - cost, 2)
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
    def make_change(self):
        if self.change == 0:
            print("")
        else:
            print(f"Here is {self.CURRENCY}{self.change} in change.")

    def get_change(self, cost):
        if self.change >= cost:
            self.change = round(self.change - cost, 2)
            self.profit += cost
            return True
        else:
            print("Sorry that's not enough money.")
            self.money_received = 0
            return False
        
    def change_amount(self):
        return self.change
