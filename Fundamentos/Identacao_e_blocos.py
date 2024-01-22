# Identação é deixar o código visivelmente melhor (são os espaços) e como regra utilizar **4 espaços**

# Blocos em Python são iniciados com ':' porém não existe algo que identifica o final, somente dando 'Enter'
#e quando o interpretador observa um inicio de linha no começo da linha sem os 4 espaços

def sacar(valor):    # Início do bloco do método (sacar), por causa do ':'
    saldo = 500

    if saldo >= valor:
        print("valor sacado!")
        print("retire o seu dinheiro na boca do caixa.")

    print("Obrigado por ser nosso cliente, tenha um bom dia!")


def depositar(valor):
    saldo = 500
    saldo += valor

sacar(900)        # Valor de referencia para ver se a condicional IF será executado ou não
