#           Desafio Iniciante
# Elaborar um sistema bancário com função de Depósito, Saque e Extrato que armazene os valores
# dos depósitos e saques realizados.

# Os valores depositados e sacados devem ser positivos e serem exibidos no extrato

# O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque.

# Se o usuário não tiver saldo em conta, deverá exibir na tela uma mensagem informando que não será possível
# realizar o saque

# Possua um limite máximo de 3 saques diários, sendo que cada saque tenha um limite de R$ 500,00

# No extrato além de mostrar as operações de depósito e de saque, deve ser exibido o saldo atual da conta e se
# não houver tido transações, exibir a mensagem "Não foram realizadas movimentações."

# Todos os valores devem ser exibidos em formato de real, ou seja com o R$

menu = """
####################################
Digite a opção desejada da operação:

[1] Depositar 
[2] Sacar
[3] Extrato
[0] Sair
####################################
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "1":
        print("############# Depósito #############")        
        deposito = float(input("Informe o valor a ser depositado: R$ "))
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: ----------- R$ {deposito:.2f}\n"
            print(f"Saldo: R$ {saldo:.2f}")
        else:
            print("Operação falhou, pois o valor de depósito é inválido")

    elif opcao == "2":
        print("############# Saque #############")
        print(f"Seu saldo atual é de: R$ {saldo}\n")
        saque = float(input("Informe o valor do saque: R$ "))

        excedeu_saldo = saque > saldo

        excedeu_limite = saque > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print(f"Não será possível realizar o saque por falta de saldo, verifique o saldo atual: R$ {saldo:.2f}")
           
        elif excedeu_limite:
            print("Limite de saque por operação é de R$ 500,00. \n\t\t Por favor repetir!")

        elif excedeu_saques:
            print("Você excedeu o número máximo de 3 saques diários")

        elif saque > 0:
            saldo -= saque
            extrato += f"Saque: -------------- R$ {saque:.2f}\n"
            numero_saques += 1
            print(f"Saque realizado com sucesso!\nVocê ainda possui {numero_saques} saques hoje")
            print(f"Saldo:  RS {saldo:.2f}")

        else:
            print("Operação falhou, pois o valor de saque é inválido")     

    elif opcao == "3":
        print("############# Extrato #############")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("###################################")


    elif opcao == "0":
        print("\t Obrigado por utilizar nosso Banco e ser nosso cliente.\n\t\t\t Até a próxima!\n")
        break

    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")