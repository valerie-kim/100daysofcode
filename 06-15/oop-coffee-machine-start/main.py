from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

off = False
while not off:
    options = menu.get_items()
    choice = input(f"What do you want to have? ({options}): ")
    if choice== "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        off = True
    else:
        drink = menu.find_drink(choice)
        is_enough_resources = coffee_maker.is_resource_sufficient
        is_enough_money = money_machine.make_payment(drink.cost)
        if is_enough_resources and is_enough_money:
            coffee_maker.make_coffee(drink)

            
        
            
    
    
    