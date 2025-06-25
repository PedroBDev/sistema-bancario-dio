def parse_input_tipo_conta():
    while True:
        tipo_conta = input('Informe o tipo de conta: [P] - Poupança / [C] - Corrente: ').strip().upper()
        if tipo_conta == 'C':
            return 'Corrente'
        elif tipo_conta == 'P':
            return 'Poupança'
        else:
            print("Entrada inválida. Por favor, digite 'P' para Poupança ou 'C' para Corrente.")
