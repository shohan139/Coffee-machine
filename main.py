# [Q]: this MenuItem should not be imported AFAIK
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from time import sleep

def welcome():
    print('''\033[33m
             )))
            (((
          +-----+
          |     |] - WELCOME TO THE COFFEE MACHINE!
          `-----' 
    
          ------ MENU ------ 
          Espresso ($1.50)
          Latte ($2.50)
          Cappuccino ($3.00)
          ------------------
    
          PS: Type "report" at any moment
          to check our resources available.
          Type "off" to log out from the machine.\033[m
        ''')



menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
is_on = True

# TODO: you should stay in the loop till the user cleary exit by clicking the "Exit" menu voice
while is_on:
    welcome()
    options = menu.get_items()

    user_choice = str(input(f"What would you like?\nOptions ({options}): ")).strip().lower()
    
    if user_choice == "off":
        print("\033[31m<<THE END>>\033[m")
        break
    else:
        beverage = menu.find_drink(user_choice) # Encapsulates the result
        if beverage == 0:
            break
        sufficient_resources = coffee_maker.is_resource_sufficient(beverage)  # TrueFalse result
        sufficient_money = money_machine.make_payment(beverage.cost)  # Encapsulates
        # FIXME: there is no point in checking for sufficient_money if you don't have enough resources to make the coffee. Add a check after each function invocation and immediately exit as soon as you find a blocker.
        if sufficient_resources and sufficient_money:
            print("Thank you! Allow us to make your beverage now..")
            coffee_maker.make_coffee(beverage)
            sleep(5)
