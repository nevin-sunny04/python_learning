from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_Machine = MoneyMachine()
coffee_Maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(coffee_Maker.report())
        print(money_Machine.report())
    else:
        drink = menu.find_drink(choice)
        payment = money_Machine.make_payment(drink.cost)
        if payment and coffee_Maker.is_resource_sufficient(drink):
            coffee_Maker.make_coffee(drink)