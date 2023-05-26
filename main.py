import operacoes

saldo = 0
extrato = []
deposito = 0
LIMITE_DE_SAQUE = 3

while True:
    menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Diqite a opção desejada: 
'''
    opcao = input(menu)
    #depositar
    if opcao == 'd':
        deposito = int(input('Qual o valor que deseja depositar? '))
        saldo = operacoes.depositar(deposito, saldo, extrato)

    #sacar 
    #condicoes: apenas 3 saques diarios; limite maximo de 500 por saque;
    #caso nao tenha saldo em conta, mostrar mensagem de saldo insuficiente
    if opcao == 's':
        saque = int(input("Qual o valor que deseja sacar? "))
        saldo, extrato, LIMITE_DE_SAQUE = operacoes.sacar(saque, LIMITE_DE_SAQUE, saldo, extrato)
        print(f"Saldo atual: {saldo}", f"Limite de saques diários restantes: {LIMITE_DE_SAQUE}")

    #visualizar extrato
    if opcao == 'e':
         print(extrato)
         print(f'Seu saldo atual: {saldo:.2f}')

    #finalizar programa
    if opcao == 'q':
        exit("Programa finalizado.")
