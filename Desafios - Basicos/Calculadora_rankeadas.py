            ## Calculadora de partidas Rankeadas ##

## **O Que deve ser utilizado**

# - Variáveis
# - Operadores
# - Laços de repetição
# - Estruturas de decisões
# - Funções

## Objetivo:

# - Crie uma função que recebe como parâmetro a quantidade de vitórias e derrotas de um jogador,
# depois disso retorne o resultado para uma variável, na qual o saldo de Rankeadas deve ser feito
# através do calculo (vitórias - derrotas)

# Se vitórias for menor do que 10 = Ferro
# Se vitórias for entre 11 e 20 = Bronze
# Se vitórias for entre 21 e 50 = Prata
# Se vitórias for entre 51 e 80 = Ouro
# Se vitórias for entre 81 e 90 = Diamante
# Se vitórias for entre 91 e 100= Lendário
# Se vitórias for maior ou igual a 101 = Imortal

## Saída

# Ao final deve se exibir uma mensagem:
# "O Herói tem de saldo de **{saldoVitorias}** está no nível de **{nivel}**"

vitorias = int(input("\nDigite a quantidade de vitórias: "))
derrotas = int(input("\nDigite a quantidade de derrotas: "))

def calcular_rank(vitorias, derrotas):
    saldo_vitorias = vitorias - derrotas

    if saldo_vitorias > 0:
        if saldo_vitorias < 10:
            nivel = "Ferro"
        elif 10 <= saldo_vitorias <= 20:
            nivel = "Bronze"
        elif 21 <= saldo_vitorias <= 50:
            nivel = "Prata"
        elif 51 <= saldo_vitorias <= 80:
            nivel = "Ouro"
        elif 81 <= saldo_vitorias <= 90:
            nivel = "Diamante"
        elif 91 <= saldo_vitorias <= 100:
            nivel = "Lendário"
        else:
            nivel = "Imortal"

        mensagem = f"\nO Herói tem um saldo de {saldo_vitorias} vitórias e está no nível de {nivel}\n"
    else:
        mensagem = "\nO herói não possui vitórias suficientes para possuir um rank. Ainda é iniciante, continue lutando\n"

    return mensagem

   

resultado = calcular_rank(vitorias, derrotas)

print(resultado)