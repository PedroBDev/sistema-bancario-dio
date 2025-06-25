
from datetime import datetime, timedelta
from utils import parse_input_tipo_conta

class Conta:
    def __init__(self, numero_conta, saldo=0, limite_saque=3, limite_valor=500.00, registro=None, tipo_conta = 'Corrente'):
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.limite_saque = limite_saque
        self.limite_valor = limite_valor
        self.registro = registro if registro is not None else []
        self.tipo_conta = tipo_conta

    def deposito(self, valor_deposito):
        self.saldo+=valor_deposito
        data_deposito = datetime.now()
        registro_deposito = {'Operacao': 'Déposito', 'Valor':valor_deposito, 'Data': data_deposito}
        
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
                    data_saque = datetime.now()
                    registro_saque = {'Operacao':'Saque', 'Valor':valor_saque, 'Data': data_saque}
                    self.registro.append(registro_saque)

    def extrato(self):
        for operacao in self.registro:
            print(f'{operacao['Operacao']}: {operacao['Valor']}')

    @staticmethod
    def criar_conta(digito):
        agencia = "0001-"
        tipo_conta = parse_input_tipo_conta()
        digito_conta = str(digito)
        num_conta = agencia + digito_conta
        conta = Conta(numero_conta=num_conta, tipo_conta= tipo_conta)

        return conta


class Cliente(Conta):
    def __init__(self, numero_conta, saldo, limite_saque, limite_valor, registro, info_cliente):
        super().__init__(numero_conta, saldo, limite_saque, limite_valor, registro)
        self.info_cliente= info_cliente if info_cliente is not None else []

    @staticmethod
    def criar_cliente(digito):
        agencia = "0001-"
        string_data_maioridade = datetime.now().strftime('%d/%m/%Y')
        data_maioridade = datetime.strptime(string_data_maioridade, '%d/%m/%Y') - timedelta(days=365 * 18)
        print("PARA SE CADASTRAR, PREENCHA OS DADOS ABAIXO:")
        nome = input('Nome:')
        while True:
            try:
                data_nascimento = input('informe sua data de nascimento(xx/xx/xxxx):')
                data_nascimento_novo = datetime.strptime(data_nascimento, '%d/%m/%Y')
                if data_nascimento_novo > data_maioridade:
                    info_cliente = None
                    conta = None
                    break
                else:
                    cpf = int(input('Informe seu cpf(apenas números):'))
                    logradouro = input('Informe o nome da sua Rua e o numero da sua residência(rua,n°):')
                    bairro = input('Informe o bairro:')
                    cidade = input('Informe a cidade/UF:')
                    tipo_conta = parse_input_tipo_conta()

                    endereco = f"{logradouro} - {bairro} - {cidade}"
                    digito_conta = str(digito)
                    num_conta = agencia+digito_conta

                    info_cliente = {'nome': nome, 'cpf': cpf, 'data_nascimento': data_nascimento_novo,
                                    'endereco': endereco,
                                    'num_conta': [num_conta], 'tipo_conta':[tipo_conta]}

                    conta = Conta(numero_conta=num_conta, tipo_conta=tipo_conta)
                    break

            except ValueError:
                print('Por favor, insira o formato correto')
        if conta:
            return Cliente(conta.numero_conta, conta.saldo, conta.limite_saque, conta.limite_valor, conta.registro, info_cliente)
        else:
            return None

    @staticmethod
    def acesso_conta(cliente):
        while True:
            escolha = int(input('''               --------------------------------------
                                    Bem Vindo ao Sistema Bancário

                                    [1] - Sacar
                                    [2] - Depositar
                                    [3] - Extrato
                                    [4] - Sair

                                -------------------------------------
        :'''))

            if escolha == 1:
                try:
                    valor_saque = float(input('Informe o valor do Saque:'))
                    cliente.saque(valor_saque)
                except TypeError:
                    print('Por favor, digite apenas número!')
                    continue
            elif escolha == 2:
                try:
                    valor_deposito = float(input('Informe o valor do Saque:'))
                    cliente.deposito(valor_deposito)
                except ValueError:
                    print('Por favor, digite apenas número!')
                    continue
            elif escolha == 3:
                cliente.extrato()

            else:
                break