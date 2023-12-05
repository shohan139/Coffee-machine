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
          1. Espresso ($1.50)
          2. Latte ($2.50)
          3. Cappuccino ($3.00)
          4. Exit
          ------------------
    
          \033[m
        ''')



menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
is_on = True
repeat_test = 0
second_repeat = 0

while is_on:
    welcome()
    options = menu.get_items()
    flag = 0
    try:
        user_choice = int(input(f"What would you like?\n: "))
    except:
        print("Wrong input! Please enter number shown in the menu only!")
        flag = 1
    
    if flag == 1:
        continue
    elif user_choice<=0 or user_choice>4:
        print("Please enter 1 to 4 only!")
    else:
        if user_choice == 4:
            print("\033[31m<<THE END>>\033[m")
            break
        else:
            user_choice = menu.set_items(user_choice)
            beverage = menu.find_drink(user_choice) # Encapsulates the result
            if beverage == 0:
                break
            # sufficient_resources = coffee_maker.is_resource_sufficient(beverage)  # TrueFalse result
            if repeat_test == 1:
                sufficient_money = money_machine.get_change(beverage.cost)
            else:
                sufficient_money = money_machine.make_payment(beverage.cost)  # Encapsulates
            if sufficient_money:
                print("Thank you! Allow us to make your beverage now..")
                coffee_maker.make_coffee(beverage)
                second_repeat = 1
                sleep(1)
            else:
                second_repeat = 0

            money_machine.make_change()

            while True:
                try:
                    repeat = int(input("To make another purchase, please enter 1, or 0 to end!\n:"))
                except:
                    if type(repeat) != "int":
                        print("Wrong input! Try again.")
                else:
                    if repeat < 0 or repeat > 1:
                        print("Wrong input! Try again!")
                        continue
                    else:
                        break
            if repeat == 0:
                print("\033[31m<<THE END>>\033[m")
                break
            else:
                repeat_test = 1
            change = money_machine.change_amount()

            if second_repeat == 0 or change == 0:
                repeat_test = 0
