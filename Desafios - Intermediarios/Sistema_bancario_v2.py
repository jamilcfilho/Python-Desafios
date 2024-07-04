#           Desafio Intermediário

#   Neste desafio, você terá a oportunidade de otimizar o Sistema Bancário previamente desenvolvido com o uso de 
# funções Python. O objetivo é aprimorar a estrutura e a eficiência do sistema, implementando as operações de 
# depósito, saque e extrato em funções específicas. Você terá a chance de refatorar o código existente, dividindo-o 
# em funções reutilizáveis, facilitando a manutenção e o entendimento do sistema como um todo


#       OBJETIVO GERAL
#   Separar as funções existente de saque, depósito e extrato em funções. Criar duas novas funções: Cadastrar usuário 
# (cliente) e cadastrar conta bancária.

#       DESAFIO
#   Precisamos deixar o código mais modularizado, para isso vamos criar funções para as operações existentes: sacar, 
# depositar e visualizar extrato. Além disso, para a versáo 2 do nosso sistema precisamos criar duas novas 
# funções: criar usuário (cliente do banco) e criar conta corrente (vuicular com usuário).
#   SEPARAÇÃO EM FUNÇÕES -> Devemos criar funções para todas as operações do sistema. Para exercitar tudo o que 
# aprendemos neste módulo, cada função vai ter uma regra na passagem de argumentos.
#   SAQUE -> A função de saque deve receber os argumentos apenas por nome (keyword only).
#   DEPÓSITO -> A função depósito deve receber os argumentos apenas por posição (positional only)
#   EXTRATO -> A função extrato deve receber or argumentoas por posição e nome (positional only e keyword only).

#       NOVAS FUNÇÕES
#   Precisamos criar duas novas funções: criar usuário e criar conta conrrente
#   CRIAR USUÁRIO (CLIENTE) -> O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, 
# data de nascimento, cpf e endereço. O endereço é uma string com o formato: logradouro, numero - bairro - 
# cidade/sigla do estado. Deve ser armazenados somente os números do CPF. Não podemos cadastrar dois usuários com
# o mesmo CPF.
#   CRIAR CONTA CORRENTE -> O programa deve armazenar contas em uma lista, uma conta é composto por: agência, número 
# da conta e usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuário 
# pode ter mais de uma conta, mas uma conta pertence somente a um usuário.

# DICA
# Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada 
# usuário da lista.

def menu():
    menu = """\n
    ####################################
    Digite a opção desejada da operação:

    [1] Depositar 
    [2] Sacar
    [3] Extrato
    [4] Novo usuário
    [5] Nova conta
    [6] Listar contas
    [0] Sair
    ####################################
    => """
    return input(menu)

def depositar(saldo, deposito, extrato, /): # Utilizando a '/' para indicar que é somente por posição
    if deposito > 0:
        saldo += deposito
        extrato += f"Depósito: ---------- R$ {deposito:.2f}\n"
        print("\n--- Depósito realizado com sucesso ---\n")
        print(f"Saldo: R$ {saldo:.2f}")
    else:
        print("Operação falhou, pois o valor de depósito é inválido")
    return saldo, extrato

def sacar(*, saldo, saque, extrato, limite, numero_saques, limite_saques): # Utilizando o '*' para indicar que é somente por nome
    excedeu_saldo = saque > saldo
    excedeu_limite = saque > limite
    excedeu_saque = numero_saques >= limite_saques

    if excedeu_saldo:
        print(f"Não será possível realizar o saque por falta de saldo, verifique o saldo atual: R$ {saldo:.2f}")
           
    elif excedeu_limite:
        print("Limite de saque por operação é de R$ 500,00.\n\t\tPor favor repetir!")

    elif excedeu_saque:
        print("Você excedeu o número máximo de 3 saques diários")

    elif saque > 0:
        saldo -= saque
        extrato += f"Saque: ------------- R$ {saque:.2f}\n"
        numero_saques += 1
        print(f"--- Saque realizado com sucesso ---\nVocê ainda possui {numero_saques} hoje!")
        print(f"Saldo: R$ {saldo:.2f}")

    else:
        print("Operação falhou, pois o valor de saque é inválido")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n################ Extrato ################\n")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("#########################################")

def criar_usuario(usuarios):
    cpf = input("Informe seu nº de CPF (utilize somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n--- Já existe um usuário com esse CPF! ---")
        return
    
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe seu endereço (logradouro, nº - bairro - cidade/sigla do estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco":endereco})

    print("\n--- Usuário cadastrado com sucesso ---")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf] # Compressão de listas, onde pega-se a lista de usuários e filtra se o usuario que estou perguntando naquele momento o campo CPF dele é igual ao CPF que eu passei, se for ele retorna o usuário para mim, se não for a lista fica vazia.
    return usuarios_filtrados[0] if usuarios_filtrados else None # Verifica se os usuários filtrados ele tem conteúdo, se não for uma lista vazia, ele retorna o primeiro elemento porque sempre terá um usuário só com um CPF (não pode haver 2 usuários com o mesmo CPF), se não encontrar ele retornará None

def nova_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n--- Conta criada com sucesso! ---")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n---Usuário não encontrado, fluxo de criação de conta cancelado! ---")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\n
Agência:\t{conta['agencia']}
Conta corrente:\t{conta['numero_conta']}
Titular:\t{conta['usuario']['nome']}
        """
        print("*" * 40)
        print(linha)

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta = 1


    while True:
    
        opcao = menu()

        if opcao == "1":
            deposito = float(input("Informe o valor a ser depositado: R$ "))

            saldo, extrato = depositar(saldo, deposito, extrato)
           
        elif opcao == "2":
            saque = float(input("Informe o valor do saque: R$ "))

            saldo, extrato = sacar(
                saldo = saldo,
                saque = saque,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            conta = nova_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta) # Cria a conta
                numero_conta += 1 # Realiza a operação de sempre contar +1 nos números das contas, assim nenhuma fica com número igual

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            print("\t Obrigado por utilizar nosso Banco e ser nosso cliente.\n\t\t\t Até a próxima!\n")
            break

        else:
            print("Operação inválida, por favor selecione novamente a opção desejada.")

main()