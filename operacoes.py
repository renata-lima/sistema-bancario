extrato = []
#depositar
def depositar(deposito, saldo, extrato):
    if deposito <= 0:
        print("Depósito inválido")
        saldo = saldo
    else: 
        saldo = saldo + deposito
        extrato.append(f"Depósito: {deposito}")
    return saldo 

#sacar
def sacar(saque, LIMITE_DE_SAQUE, saldo, extrato):
    limite = 500
    saldo = saldo - saque
    extrato.append(f"Saque: {saque}")
    LIMITE_DE_SAQUE = LIMITE_DE_SAQUE - 1
    
    if LIMITE_DE_SAQUE == 0:
        print("limite de saque diário atingido")   
    elif saque > limite:
        print("Limite de saque ultrapassado")       
    elif saque > saldo:
        print("Saldo insuficiente")    
    return saldo, extrato, LIMITE_DE_SAQUE