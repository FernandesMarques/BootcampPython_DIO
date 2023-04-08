
lista_saques = []
lista_depositos = []
lista_clientes = []
lista_contas = []

saldo = 5000
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
nconta = 1


def menu():
    return(f"""menu principal 
     
      [d] Depositar
      [s] Sacar
      [e] Extrato
      [nu] Cadastrar clientes
      [nc] Cadastrar conta
      [lclientes] Listar clientes
      [lcontas] Listar contas
      [ ] Digite qualquer outra tecla para fechar o sistema""")


def sacar(saldo,numero_saques, LIMITE_SAQUES, lista_saques, lista_depositos, lista_clientes, lista_contas, nconta):
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
    return (saldo, numero_saques, LIMITE_SAQUES, lista_saques, lista_depositos, lista_clientes, lista_contas, nconta)

def extrato(saldo,numero_saques, LIMITE_SAQUES, lista_saques, lista_depositos, lista_clientes, lista_contas, nconta):
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
    return (saldo, numero_saques, LIMITE_SAQUES, lista_saques, lista_depositos, lista_clientes, lista_contas, nconta)

def depositar(saldo,numero_saques, LIMITE_SAQUES, lista_saques, lista_depositos, lista_clientes, lista_contas, nconta):

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
    return (saldo, numero_saques, LIMITE_SAQUES, lista_saques, lista_depositos, lista_clientes, lista_contas, nconta)


def cadastrar_clientes(saldo,numero_saques, LIMITE_SAQUES, lista_saques, lista_depositos, lista_clientes, lista_contas, nconta):
    nome = input("Informe o nome completo:")
    cpf = input("Digite seu CPF")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa)")
    endereco = input("informe o endereço (logradouro, numero - bairro - cidade/sigla estado:) - separado por '-' ")
    lista_clientes.append({"nome" : nome , "cpf" : cpf , "data_nascimento" : data_nascimento , "endereco" : endereco})
    print("\n Usuário Cadastrado com sucesso! \n")
    return (saldo, numero_saques, LIMITE_SAQUES, lista_saques, lista_depositos, lista_clientes, lista_contas, nconta)
                     
def cadastrar_conta(saldo,numero_saques, LIMITE_SAQUES, lista_saques, lista_depositos, lista_clientes, lista_contas, nconta):
    cpf = input('Digite o CPF')
    usuario_filtrado = [usuario for usuario in lista_clientes if usuario["cpf"] == cpf]
    if usuario_filtrado:
        lista_contas.append({"cpf" : cpf, "agencia" : "0001" , "conta" : nconta})
        nconta += 1
        print("\n Conta criada com sucesso")
    return (saldo, numero_saques, LIMITE_SAQUES, lista_saques, lista_depositos, lista_clientes, lista_contas, nconta)

def listar_contas(saldo,numero_saques, LIMITE_SAQUES, lista_saques, lista_depositos, lista_clientes, lista_contas, nconta):
    print(lista_contas)
    return (saldo, numero_saques, LIMITE_SAQUES, lista_saques, lista_depositos, lista_clientes, lista_contas, nconta)

def listar_clientes(saldo,numero_saques, LIMITE_SAQUES, lista_saques, lista_depositos, lista_clientes, lista_contas, nconta):
    print(lista_clientes)
    return (saldo, numero_saques, LIMITE_SAQUES, lista_saques, lista_depositos, lista_clientes, lista_contas, nconta)

dicionario_funcoes = {
    'menu' : menu,
    's' : sacar,
    'e' : extrato,
    'd' : depositar,
    'nu' : cadastrar_clientes,
    'nc' : cadastrar_conta,
    'lclientes' : listar_clientes,
    'lcontas' : listar_contas
}



while True:
    print(dicionario_funcoes['menu']())

    opcao= str(input())    
    if opcao != 's' and opcao != 'e' and opcao != 'd' and opcao != 'nu' and opcao != 'nc' and opcao != 'lclientes' and opcao != 'lcontas':
        print('''Obrigado por usar nosso sistema!
--#--------------#-----------#-----------#-----------#-----------''')
        break
    else:
        saldo, numero_saques, LIMITE_SAQUES, lista_saques, lista_depositos, lista_clientes, lista_contas, nconta = dicionario_funcoes[opcao](saldo, numero_saques, LIMITE_SAQUES, lista_saques, lista_depositos, lista_clientes, lista_contas, nconta)
        
            
        



    
