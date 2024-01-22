def verifica_encaixe(A, B):
    # Verifica se os últimos dígitos de A são iguais a B
    if A.endswith(B):
        return "encaixa"
    else:
        return "nao encaixa"

# Função principal
def main():
    # Número de casos de teste
    N = int(input())

    # Lista para armazenar os casos de teste como strings
    casos_teste = []

    for _ in range(N):
        # Entrada dos valores A e B
        A, B = input().split()
        casos_teste.append((A, B))

    # Itera sobre os casos de teste e imprime o resultado
    for caso in casos_teste:
        resultado = verifica_encaixe(caso[0], caso[1])
        print(resultado)

# Chamando a função principal
if __name__ == "__main__":
    main()
