#             DESAFIO INTERMEDIÁRIO - PYTHON DEVELOPER

#       Desafio
#   Imagine que você está trabalhando em um sistema de gerenciamento de estoque que recebe dados de produtos de
# uma API externa. Cada produto é representado por uma string que contém seu nome, preço e a quantidade
# disponível em estoque. Por exemplo, a string "Laptop:1200:10;Mouse:20:0;Keyboard:50:5" indica que há 10 unidades
# do laptop disponíveis, 0 unidades do mouse e 5 unidades do teclado.

#   Seu objetivo é implementar uma função em Python que filtre apenas os produtos que têm quantidade maior que
# zero. A função deve então retornar uma lista de strings, onde cada string representa um produto disponível,
# no formato original "NOME:PRECO:QUANTIDADE".

#       Entrada
#   A entrada deve receber uma lista de strings contendo o nome do produto, preço e a quantidade disponível
# em estoque, separados por “:” respectivamente.

#       Saída
#   Deverá retornar uma lista de strings, onde cada string contém as informações dos produtos que têm quantidade
# maior que 0.


# Recebe a entrada e armazena na variável "entrada"
entrada = input()


# Função responsável por filtrar produtos em estoque
def filtrar_produtos_em_estoque(entrada):
    if not entrada:
        return []

    produtos = entrada.split(';')
    produtos_disponiveis = []

    for produto_str in produtos:
        # Divida a substring do produto em nome, preço e quantidade usando ':' e converta a quantidade para inteiro
        nome, preco, quantidade = produto_str.split(":")
        quantidade = int(quantidade)

        # Verifique se a quantidade é maior que zero, caso seja adicione o produto à lista de produtos disponíveis
        if quantidade > 0:
            produtos_disponiveis.append(produto_str)

    return produtos_disponiveis


# Imprime a lista de produtos em estoque
print(filtrar_produtos_em_estoque(entrada))
