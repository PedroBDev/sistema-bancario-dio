class Conta:
    def __init__(self, saldo = 0, limite_saque = 3, limite_valor = 500.00, registro=None):
        self.saldo = saldo
        self.limite_saque = limite_saque
        self.limite_valor = limite_valor
        self.registro = registro if registro is not None else []

    def deposito(self, valor_deposito):
        self.saldo+=valor_deposito
        registro_deposito = {'Operacao': 'Déposito', 'Valor':valor_deposito}
        self.registro.append(registro_deposito)

    def saque(self, valor_saque):
        if valor_saque > self.saldo:
            print('Você não tem saldo suficiente')
        else:
            if self.limite_saque<1:
                print('Você excedeu a quantidade de saques diários')
            else:
                if valor_saque > self.limite_valor:
                    print('Você excedeu o limite de valor em uma transferência!')
                else:
                    self.saldo -= valor_saque
                    self.limite_saque-=1
                    print('Saque realizado com sucesso.', '\n', f'Saldo atual:{self.saldo}')
                    registro_saque = {'Operacao':'Saque', 'Valor':valor_saque}
                    self.registro.append(registro_saque)

    def extrato(self):
        for operacao in self.registro:
            print(f'{operacao['Operacao']}: {operacao['Valor']}')