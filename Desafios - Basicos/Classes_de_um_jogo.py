            ## Escrevendo as classes de um Jogo ##

## **O Que deve ser utilizado**

# - Variáveis
# - Operadores
# - Laços de repetição
# - Estruturas de decisões
# - Funções
# - Classes e Objetos

## Objetivo:

# - Crie uma classe generica que represente um herói de uma aventura e que possua as seguintes propriedades:
# nome
# idade
# tipo (ex: guerreiro, mago, monge, ninja )

# - Além disso, deve ter um método chamado atacar que deve atender os seguientes requisitos:
# exibir a mensagem: "o {tipo} atacou usando {ataque}")
# aonde o {tipo} deve ser concatenando o tipo que está na propriedade da classe
# e no {ataque} deve seguir uma descrição diferente conforme o tipo, seguindo a tabela abaixo:
# se mago -> no ataque exibir (usou magia)
# se guerreiro -> no ataque exibir (usou espada)
# se monge -> no ataque exibir (usou artes marciais)
# se ninja -> no ataque exibir (usou shuriken)

## Saída

# Ao final deve se exibir uma mensagem:
# -> "o {tipo} atacou usando {ataque}"
# ex:"o mago atacou usando magia"
# ex:"o guerreiro atacou usando espada"


# Criando a classe que recebe o nome de Heroi (boas práticas utilizar CamelCase)
class Heroi:
    def __init__(self, nome, idade, tipo, ataque):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
        self.ataque = ataque

# Definindo uma função "atacar" dentro da classe "Heroi"
    def atacar(self):
            if self.ataque == 0:
                SystemExit
            else:
                print(f"O {self.nome} com {self.idade} anos, é um {self.tipo.lower()} que atacou usando {self.ataque}")




nome = input("Defina o nome do seu herói: ")
idade = int(input("Defina a idade do seu herói: "))
tipo = input("Escolha e digite a respectiva classe entre: Guerreiro, Mago, Monge e Ninja:\n")

if tipo == "Guerreiro":
    ataque = "espada"

elif tipo == "Mago":
    ataque = "magia"

elif tipo == "Monge":
    ataque = "artes marciais"

elif tipo == "Ninja":
    ataque = "shuriken"

else:
    ataque = 0
    print("Respeite os caracteres maiúsculo e minúsculo e digite a classe novamente!!!")
    

# Definindo um objeto "acao"
acao = Heroi(nome, idade, tipo, ataque)

# Executando o objeto
acao.atacar()