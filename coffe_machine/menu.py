class MenuItem:

    '''
    Classe para a construção dos itens do menu.

    Args:
    name -> str
    cost -> float
    ingredients -> dictionary 
    '''
    def __init__(self, name, water, milk, coffe, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffe": coffe
        }

class Menu:

    '''
    Classe contendo todas as especificações de ingredientes necessários e preço de cada opção de café.
    '''

    def __init__(self):
        '''
        Função para especificar a quantidade de cada ingrediente presente em cada café e seu preço.
        '''
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffe=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffe=18, cost=1.5),
            MenuItem(name="capuccino", water=250, milk=50, coffe=24, cost=3)
        ]


    def get_items(self):
        '''
        Função para obter os nomes dos itens do Menu.

        Retorno:
        options = nome de todos os itens do Menu em uma string concatenada -> latte/espresso/cappuccino
        '''
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options
    
    def find_drinks(self, order_name):
        '''
        Função para buscar determinado item por nome. 
        
        Retornos:
        item = nome do tipo de café
        None -> item inexistente  
        '''
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry, that item is not available.")