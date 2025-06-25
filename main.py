from conta import Cliente, Conta
lista_cliente = []
info_cliente = None
digito = 0
def checar_cliente(cpf):
    for cliente in lista_cliente:
            if cpf == cliente['cpf']:
                return True
            else:
                return False

while True:
    print('Bem vindo ao nosso Banco!!')
    escolha = int(input('[1] - Realizar cadastro/ [2] - Criar Conta/ [3] - Acessar conta/ [4] - Sair '))

    if escolha == 1 :
        digito+=1
        info_cliente = Cliente.criar_cliente(digito)
        if info_cliente is None:
            print('Você é menor de idade, portanto, não é possível realizar o cadastro!')
            break
        else:
            if checar_cliente(cpf = info_cliente.info_cliente['cpf']):
                print('Usuário já cadastrado!')
                continue
            else:
                lista_cliente.append(info_cliente.info_cliente)
                print(lista_cliente)

    elif escolha == 2:
       cpf_input = int(input('Informe seu cpf(sem pontos ou tracos, apenas números):'))
       print(type(cpf_input))
       if checar_cliente(cpf_input):
           for cliente_encontrado in lista_cliente:
               if cpf_input== cliente_encontrado['cpf']:
                   digito+=1
                   conta = Conta.criar_conta(digito)
                   cliente_encontrado['num_conta'].append(conta.numero_conta)
                   cliente_encontrado['tipo_conta'].append(conta.tipo_conta)
       else:
           print("Por favor, cadastre-se!")



    elif escolha == 3:
        if info_cliente:
            info_cliente.acesso_conta(info_cliente)
        else:
            print("Por favor, cadastre-se!")

    elif escolha == 4:
        break

    else:
        print('informe uma opção válida')
        continue
    

        

