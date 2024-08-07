#             DESAFIO INTERMEDIÁRIO - PYTHON DEVELOPER

#       Desafio
#   Uma empresa de marketing deseja segmentar seus clientes para uma nova campanha promocional. A empresa fornece uma lista de clientes,
# cada um com seu nome e cidade. Sua tarefa é filtrar os clientes que moram em uma cidade específica.

#       Entrada
#   A entrada consiste em duas partes:
#   1. Uma string representando a cidade de interesse para a campanha.
#   2. Uma string contendo o nome do cliente (string) e a cidade do cliente (string), no seguinte formato: "CLIENTE:CIDADE;CLIENTE:CIDADE;..."

#       Saída
#   O programa deverá retornar uma lista de tuplas contendo os clientes que moram na cidade especificada.


# Recebe a cidade de interesse da entrada do usuário e remove espaços em branco nas extremidades
cidade_interesse = input().strip()
# Recebe a lista de clientes da entrada do usuário e remove espaços em branco nas extremidades
clientes = input().strip()


# Função que filtra os clientes que moram na cidade especificada
def filtrar_clientes(lista_clientes, cidade_interesse):
    # Se a lista de clientes estiver vazia, retorna uma lista vazia
    if not lista_clientes:
        return []

    # Inicializa uma lista vazia para armazenar os clientes filtrados
    clientes_filtrados = []

    # Percorra cada tupla (nome, cidade) na lista de clientes
    for nome, cidade in lista_clientes:
        # Se a cidade do cliente for igual à cidade de interesse, adicione a tupla (nome, cidade) na lista de clientes filtrados
        if cidade.strip() == cidade_interesse:
            clientes_filtrados.append((nome.strip(), cidade.strip()))

    return clientes_filtrados


# Processa a entrada de clientes para converter a string de clientes em uma lista de tuplas (nome, cidade)
lista_clientes = [tuple(cliente.split(':')) for cliente in clientes.split(';')]

# Imprime a lista de clientes filtrados
print(filtrar_clientes(lista_clientes, cidade_interesse))
