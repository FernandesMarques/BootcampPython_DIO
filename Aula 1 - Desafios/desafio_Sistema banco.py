
lista_saques = []
lista_depositos = []
saldo = 5000
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3


def menu():
    return(f"""menu principal - SALDO ATUAL R${saldo}
     
      [d] Depositar
      [s] Sacar
      [e] Extrato
      [ ] Digite qualquer outra tecla para fechar o sistema""")


def sacar(saldo,numero_saques, LIMITE_SAQUES, lista_saques, lista_depositos):
    print("-----------------------------sacar-----------------------------")
    print(f"Seu saldo é R${saldo}")
    if saldo > 0:
        valor_saque = float(input('Digite o valor que deseja sacar: R$'))
        if valor_saque <= saldo and valor_saque <= 500 and numero_saques < LIMITE_SAQUES:
            saldo = saldo - valor_saque
            numero_saques = numero_saques + 1
            lista_saques.append(valor_saque)
            print(f"""Valor sacado com sucesso! 
Seu saldo agora é de R${saldo}
Digite qualquer valor para ser redirecionado ao menu principal""")
            
        else:
            print(f"""ERRO! Alguma das irregularidades foi encontrada
-Você não possui o valor solicitado em conta - SALDO R${saldo}
-Valor excede o limite de R$500 - VALOR DO SAQUE R${valor_saque}
-Limite máximo de saques alcançado - SAQUES EFETUADOS {numero_saques} - Limite de saques {LIMITE_SAQUES}
Digite qualquer valor para ser redirecionado ao menu principal""")
        input()
    else:
        print("""Você não possui saldo suficiente para realizar um saque. 
        Digite qualquer valor para ser redirecionado ao menu principal""")
        input()
    return (saldo, numero_saques, LIMITE_SAQUES, lista_saques, lista_depositos)

def extrato(saldo,numero_saques, LIMITE_SAQUES, lista_saques, lista_depositos):
    print("-----------------------------extrato-----------------------------")
    print("Os valores depositados foram:")
    for extrato_deposito in lista_depositos:
        print(f"R${extrato_deposito}")
    print("""
---------------------------------------------------------------
             Os valores depositados foram:""")
    for extrato_saque in lista_saques:
        print(f"R${extrato_saque}")
    print(f"""
---------------------------------------------------------------
Seu saldo é: R${saldo}
Seu limite de saques é: {LIMITE_SAQUES} saques
Você realizou: {numero_saques} saques
             
Digite qualquer valor para ser redirecionado ao menu principal
             """)
    input()
    return (saldo, numero_saques, LIMITE_SAQUES, lista_saques, lista_depositos)

def depositar(saldo,numero_saques, LIMITE_SAQUES, lista_saques, lista_depositos):
    print("-----------------------------sacar-----------------------------")
    print(f"Seu saldo é R${saldo}")
    valor_deposito = float(input('Digite o valor que deseja depositar: R$'))
    if valor_deposito > 0:
        saldo = saldo + valor_deposito
        lista_depositos.append(valor_deposito)
        print(f"""
Depósito feito com sucesso! Seu novo saldo é: R${saldo}
Digite qualquer valor para ser redirecionado ao menu principal""")
        
    else:
        print("""
Valor de depósito invalido, 
Digite qualquer valor para ser redirecionado ao menu principal""")
    
    input()
    return (saldo, numero_saques, LIMITE_SAQUES, lista_saques, lista_depositos)

dicionario_funcoes = {
    'menu' : menu,
    's' : sacar,
    'e' : extrato,
    'd' : depositar
}



while True:
    print(dicionario_funcoes['menu']())

    opcao= str(input())    
    if opcao != 's' and opcao != 'e' and opcao != 'd':
        print('''Obrigado por usar nosso sistema!
--#--------------#-----------#-----------#-----------#-----------''')
        break
    else:
        saldo, numero_saques, LIMITE_SAQUES, lista_saques, lista_depositos = dicionario_funcoes[opcao](saldo, numero_saques, LIMITE_SAQUES, lista_saques, lista_depositos)
        
            
        



    
