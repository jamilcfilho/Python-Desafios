#             DESAFIO BÁSICO 1/3 - PYTHON DEVELOPER

# O microblog Twitter é conhecido por limitar as postagens em 140 caracteres. 
# Conferir se um texto vai caber em um tuíte é sua tarefa.

# ENTRADA
# A entrada é uma linha de texto T (1 ≤ |T| ≤ 500).

# SAÍDA
# A saída é dada em uma única linha.
# Ela deve ser "TWEET" (sem as aspas) se a linha de texto T tem até 140 caracteres.
# Se T tem mais de 140 caracteres, a saída deve ser "MUTE".

T = input("Digite a sua postagem: ")

if len(T) <= 140:   # função LEN(), tem a função de realizar a contagem de itens em determinado objeto
    print("TWEET")
else:
    print("MUTE")