from menu import Menu
from coffe_maker import CoffeMaker
from money_machine import MoneyMachine

#Criando os objetos
menu = Menu()
coffe_maker = CoffeMaker()
money = MoneyMachine()

#Unindo os objetos
is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffe_maker.report()
        money.report()
    else:
        drink = menu.find_drinks(choice)
        if coffe_maker.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffe_maker.make_coffe(drink)
        
