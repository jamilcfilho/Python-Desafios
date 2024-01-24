#             DESAFIO BÁSICO 3/3 - PYTHON DEVELOPER

# Paulinho tem em suas mãos um novo problema.
# Agora a sua professora lhe pediu que construísse um programa para verificar,
# à partir de dois valores muito grandes A e B, se B corresponde aos últimos dígitos de A.

# ENTRADA
# A entrada consiste de vários casos de teste.
# A primeira linha de entrada contém um inteiro N que indica a quantidade de casos de teste.
# Cada caso de teste consiste de dois valores A e B maiores que zero, cada um deles podendo ter até 1000 dígitos.

# SAÍDA
# Para cada caso de entrada imprima uma mensagem indicando se o segundo valor encaixa no 
# primeiro valor.

def verifica_encaixe(a, b): #Função -> verifica_encaixe
    if len(b) > len(a):
        return "nao encaixa"
    elif a.endswith(b):
        return "encaixa"
    else:
        return "nao encaixa"

# Quantidade de casos de teste que deverá ocorrer
N = int(input("Digite a quantidade de casos de teste: "))

# Itera sobre cada caso de teste
for i in range(N):
    a = input("Digite o valor de A: ")
    b = input("Digite o valor de B: ")

    # Chama a função e imprime o resultado
    resultado = verifica_encaixe(a, b)
    print(resultado)
