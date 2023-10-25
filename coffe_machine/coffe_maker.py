class CoffeMaker:
    '''
    Classe para executar todo o processo de confecção dos cafés.
    '''

    def __init__(self):
        '''
        Função para determinar a quantidade dos ingredientes da máquina.
        '''
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffe": 100
        }

    def report(self):
        '''
        Função para reportar quanto temos de cada ingrediente.

        Args:
        resources -> int
        '''
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffe: {self.resources['coffe']}g")

    def is_resource_sufficient(self, drink):
        '''
        Função para determinar se temos ingredientes suficientes para confeccionar o café solicitado.

        Args:
        can_make -> bool

        Retornos: 
        True = ingredientes SUFICIENTES 
        False = ingredientes INSUFICIENTES
        '''
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make
    
    def make_coffe(self, order):
        '''
        Função para a confecção dos cafés.
        '''
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")