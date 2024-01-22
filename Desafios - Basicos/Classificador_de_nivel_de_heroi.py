#                Desafio Classificador de nível de Herói

# **O Que deve ser utilizado**

# - Variáveis
# - Operadores
# - Laços de repetição
# - Estruturas de decisões

#                              Objetivo

# Crie uma variável para armazenar o nome e a quantidade de experiência (XP) de um herói, depois utilize
# uma estrutura de decisão para apresentar alguma das mensagens abaixo:

# Se XP for menor do que 1.000 = Ferro
# Se XP for entre 1.001 e 2.000 = Bronze
# Se XP for entre 2.001 e 5.000 = Prata
# Se XP for entre 5.001 e 7.000 = Ouro
# Se XP for entre 7.001 e 8.000 = Platina
# Se XP for entre 8.001 e 9.000 = Ascendente
# Se XP for entre 9.001 e 10.000= Imortal
# Se XP for maior ou igual a 10.001 = Radiante

## Saída

# Ao final deve se exibir uma mensagem:
# "O Herói de nome **{nome}** está no nível de **{nivel}**"

nome_do_heroi = input("Digite um nome para seu herói: ")
experiencia_heroi = int(input("\nDigite o total de experiência do seu herói: "))

if experiencia_heroi > 0 and experiencia_heroi < 1000:
    nivel = "Ferro"
        
elif experiencia_heroi >= 1000 and experiencia_heroi <= 2000:
    nivel = "Bronze"
        
elif experiencia_heroi >= 2001 and experiencia_heroi <= 5000:
    nivel = "Prata"
        
elif experiencia_heroi >= 5001 and experiencia_heroi <= 7000:
    nivel = "Ouro"
        
elif experiencia_heroi >= 7001 and experiencia_heroi <= 8000:
    nivel = "Platina"
      
elif experiencia_heroi >= 8001 and experiencia_heroi <= 9000:
    nivel = "Ascendente"
        
elif experiencia_heroi >= 9001 and experiencia_heroi <= 10000:
    nivel = "Imortal"
        
else:
    nivel = "Radiante"

print(f"O herói de nome {nome_do_heroi} está no nível {nivel}")