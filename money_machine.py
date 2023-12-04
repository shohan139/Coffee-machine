class MoneyMachine:
    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        # TODO: we should return this profit somewhere in the code, otherwise it's useless.
        self.profit = 0
        self.money_received = 0

    def report(self):
        # Prints the current profit
        print(f"Money: {self.CURRENCY}{self.profit}")
    
    def process_coins(self):
        # Returns the total calculated from inserted
        print('''\033[33m
        We accept the following coins:
        Quarters ($0.25), dimes ($0.10)
        nickles ($0.05),  pennies ($0.01)\033[m
        ''')

        self.money_received =0

        for coin in self.COIN_VALUES:
            user_input = input(f"How many {coin}? Please: ")
            try:
                num_coins = int(user_input)
                if num_coins < 0:
                    print("Wrong input")
                    return
                self.money_received += num_coins * self.COIN_VALUES[coin]
            except ValueError:
                # FIXME: be more descriptive toward the user when this error happens.
                print("Wrong input")
                return 
        print(f"You have provided: {self.CURRENCY}{self.money_received}")
        # [Q]: are you sure you have to return this value from this function? Or it's enough to set it on the instance? Maybe it's a just a silly question...
        return self.money_received
    
    def make_payment(self, cost):
        # Return True when payment is accepted, False if insufficient
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
