#             DESAFIO BÁSICO - PYTHON DEVELOPER

#       Desafio

#       Descrição
#   O desafio consiste em adicionar à função contar_caracteres a um dicionário vazio chamado contador para
# armazenar as contagens de caracteres. Vamos iterar através de cada caractere na string = 'string'. Para cada
# caractere, verifique se ele já está presente no dicionário contador. Se estiver, incremente o valor associado
# a essa chave. Caso contrário, adicione a chave ao dicionário com valor inicial 1. Neste dicionário, as chaves
# são os caracteres presentes na string e os valores correspondem à contagem de vezes que cada caractere aparece.


#       Entrada
#   A função espera receber uma única string como entrada. Neste desafio, consideramos como casos de teste apenas
# strings textuais.

#       Saída
#   A função retorna um dicionário onde cada chave é um caractere presente na string de entrada e o valor
# associado a cada chave é a quantidade de vezes que o caractere ocorre na string.

def contar_caracteres(string):
    # Inicializando um dicionário vazio para realizar a contagem dos caracteres
    contador = {}
    # Iterando através de cada caractere na string 'sring'
    for caractere in string:

        # Para cada caractere presente no dicionário contador incremente 1
        if caractere in contador:
            contador[caractere] += 1

        # Caso contrário, adiciona a chave ao dicionário com valor inicial de 1
        else:
            contador[caractere] = 1
    return contador


# Solicita entrada do usuário
entrada = input()
resultado = contar_caracteres(entrada)

print(resultado)
