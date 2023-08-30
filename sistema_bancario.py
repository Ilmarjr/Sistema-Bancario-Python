menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
saldo = 0
limite = 500
extrato =''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'q':
        break

    elif opcao == 'd':
        valor = float(input('Valor do depósito: '))
        if valor < 0:
            print('Operação falhou! o valor informado é inválido')
        else:
            saldo += valor
            print('Depósito realizado com sucesso')
            extrato += f'Depósito: R$ {valor:.2f}\n'

    elif opcao =='s':

        valor = float(input('Valor do saque: '))
        if valor < 0:
            print('Operação falhou! o valor informado é inválido')
        elif numero_saques >= 3:
            print('Operação falhou! o limite diário de saques foi atingido')
        elif valor > 500:
            print(f'Operação falhou! Valor do saque excede o limite de {limite}, tente um valor válido')
        elif valor > saldo:
            print('Operação falhou! Saldo Insuficiente')
        else:
            saldo -= valor
            numero_saques += 1
            print('Saque realizado com sucesso')
            extrato += f'Saque: R$ {valor:.2f}\n'
        
    elif opcao == 'e':
        print("\n=============== EXTRATO =================")
        print("\nNão houve movimentações." if not extrato else extrato)
        print(f'Saldo: R$ {saldo:.2f}')

    else: print("\nOperação inválida! Selecione outra operação.")
        