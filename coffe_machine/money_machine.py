class MoneyMachine:

    '''
    Classe para a construção do sistema de cobrança da Coffe Machine.
    '''

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        '''
        Função para calcular o lucro de acordo com o dinheiro em caixa.
        '''
        self.profit = 0 #lucro
        self.money_received = 0 

    def report(self):
        '''
        Função para obter o lucro.
        '''
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        '''
        Função para obter o saldo total de dinheiro da máquina de acordo com as moedas recebidas.

        Retorno:
        self.money_received = saldo total de dinheiro da máquina
        self.money_received -> float
        '''
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received
    
    def make_payment(self, cost):
        '''
        Função para validar o pagamento. 
        
        Retornos:
        True = quantia de dinheiro SUFICIENTE para fazer o café 
        False = quantia de dinheiro INSUFICIENTE para fazer o café 
        '''

        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
         
        print("Sorry that's not enough money. Money refunded.")
        self.money_received = 0
        return False