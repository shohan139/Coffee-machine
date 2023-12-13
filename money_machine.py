class MoneyMachine:
    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickels": 0.05,
        "pennies": 0.01
    }

    QUARTER_LIMIT = 20

    def __init__(self):
        self.profit = 0
        self.money_received = 0
        self.change = 0

    def report(self):
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self, cost, n):
        if n >= cost:
            return n
        else:
            while True:
                try:
                    self.money_received = float(input('\033[33mHow many dollar (1.00) would you like to enter? (limit: $20) : \033[m'))
                except ValueError:
                    print("Wrong input! Try again")
                    continue
                
                if self.money_received <= 0 or self.money_received > 20:
                    print(f"Please enter {self.CURRENCY}1 to {self.CURRENCY}20 only! ")
                    continue

                self.money_received = n + self.money_received

                # If the entered amount is less than the cost, ask for quarters
                if self.money_received < cost:
                    try:
                        quarters = int(input(
                            f'\033[33mHow many quarters (0.25) would you like to enter? (limit: {self.QUARTER_LIMIT}): \033[m'))
                    except ValueError:
                        print("Wrong input! Try again")
                        continue

                    if quarters < 0 or quarters > self.QUARTER_LIMIT:
                        print(f"Please enter a non-negative integer less than or equal to {self.QUARTER_LIMIT}.")
                        continue

                    self.money_received += quarters * self.COIN_VALUES["quarters"]

                break
            return self.money_received


    def make_payment(self, cost, n):
        self.total_money = self.process_coins(cost, n)
        if self.total_money >= cost:
            self.change = round(self.total_money - cost, 2)
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money.")
            self.change = self.total_money
            self.money_received = 0
            return False

    def make_change(self):
        if self.change != 0:
            print(f"You have {self.CURRENCY}{self.change} left.")

    def change_amount(self):
        return self.change
