class MoneyMachine:
    CURRENCY = "$"

    def __init__(self):
        # TODO: we should return this profit somewhere in the code, otherwise it's useless.
        self.profit = 0
        self.money_received = 0
        self.change = 0

    def report(self):
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        while True:
            try:
                self.money_received = float(input('\033[33mEnter your money: \033[m'))
            except ValueError:
                print("Wrong input! Try again")
                continue

            if self.money_received <= 0:
                print("Wrong input! Try again")
            else:
                break
        return self.money_received

    def make_payment(self, cost):
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
        if self.change != 0:
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
