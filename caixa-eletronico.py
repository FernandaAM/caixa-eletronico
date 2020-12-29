print('\nOlá, seja bem-vindo ao BANCO FEAMRS!')
deposito = 0
saque = 0
dinheiro_caixa = deposito - saque

while True:
    menu = input('\nDigite 1 para depósitos ou 2 para saques: ') #O usuário escolhe o menu de depositos ou saques
    if menu == '1':
        print('\nDigite a quantidade de notas de cada valor a ser inserido. Notas permitidas: R$10, R$20, R$50, R$100')
        notas_10 = int(input('\nNúmero de notas de R$10.00: '))
        notas_20 = int(input('Número de notas de R$20.00: '))
        notas_50 = int(input('Número de notas de R$50.00: '))
        notas_100 = int(input('Número de notas de R$100.00: '))
        deposito = notas_10 * 10 + notas_20 * 20 + notas_50 * 50 + notas_100 * 100 #Calcula quanto dinheiro o usuário depositou no caixa
        print('\nVocê depositou R$' + str(deposito) + '.00.')
    elif menu == '2':
        saque = int(input('\nDigite o valor que deseja sacar. Notas disponíveis: R$10, R$20, R$50, R$100: R$'))
        num_cedulas = 0 #Quantidade de cédulas de cada valor a ser entregue
        cedula_atual = 100 #Valor da maior cédula disponível para o valor do saque
        entregar = saque #Valor a ser entregue é o valor do saque que o usuário digitou
        while True:
            if cedula_atual <= entregar:
                num_cedulas += 1
                entregar -= cedula_atual
            else:
                if num_cedulas > 0:
                    print('%d cédula(s) de R$ %5.2f' % (num_cedulas, cedula_atual))
                if entregar == 0:
                    break
                if cedula_atual == 100:
                    cedula_atual = 50
                elif cedula_atual == 50:
                    cedula_atual = 20
                elif cedula_atual == 20:
                    cedula_atual = 10
                num_cedulas = 0
    else:
        print('\nERRO! Por favor, digite um número válido.')

    """dinheiro_caixa = deposito - saque
    if saque > dinheiro_caixa:
        print('Desculpe, saldo em caixa insuficiente.')
    else:
        print(f'O saque no valor de R${saque}.00 foi aprovado.')"""
    repetir = input('\nDeseja fazer outra operação? 1 = SIM ou 2 = NAO: ') #Opção para acessar novamente os menus
    if repetir == '2':
        print('\nObrigado! Volte sempre.')
        break
    elif repetir == '1':
        True
    else:
        print('\nERRO! Por favor, digite um número válido.')
