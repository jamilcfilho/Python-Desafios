#             DESAFIO INTERMEDIÁRIO - PYTHON DEVELOPER

#       Desafio
#   Neste desafio, temos a classe Pessoa com seus atributos que armazenam o nome e a idade de uma pessoa. Implemente
# um método para retornar uma representação formatada dos dados da pessoa, crie uma instância da pessoa e, por fim,
# chame o método para retornar as informações formatadas e imprimir o resultado. O objetivo é utilizarmos formas
# para criar e manipular objetos com POO, usando atributos e métodos para encapsular dados e comportamentos.

#       Entrada
# - Nome da pessoa (string)
# - Idade da pessoa (inteiro)

#       Saída
#   Uma string formatada com o nome e a idade da pessoa, no seguinte formato: Nome: {nome}, Idade: {idade}

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Criando um método para retornar as informações formatas com Nome e Idade:
    def pessoa(self):
        print(f"Nome: {nome}, Idade: {idade}")


# Entrada do usuário
nome = input()
idade = int(input())

# Criando uma instância da pessoa:
p1 = Pessoa(nome, idade)

# Chamando o método para retornar as informações formatadas e imprimir o resultado:
p1.pessoa()
