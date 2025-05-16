from conta import Conta

conta = Conta()
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
            conta.saque(valor_saque)
        except TypeError:
            print('Por favor, digite apenas número!')
            continue
    elif escolha == 2:
        try:
            valor_deposito = float(input('Informe o valor do Saque:'))
            conta.deposito(valor_deposito)
        except ValueError:
            print('Por favor, digite apenas número!')
            continue
    elif escolha == 3:
        conta.extrato()

    else:
        break