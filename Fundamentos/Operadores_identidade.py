# Operador de identidade serve para comparar se os valores estão no mesmo espaço de memória

# IS = 
# IS NOT = 

saldo = 1000
limite = 1000

print(saldo is limite)      # Saber se Saldo ocupa mesma região de memória de Limite, nesse exemplo SIM, pois o valor de refetencia é igual
print(saldo is not limite)

saldo1 = 1000
limite1 = 500

print(saldo1 is limite1)      # Saber se Saldo ocupa mesma região de memória de Limite, nesse exemplo Não, pois o valor de referencia e diferente
print(saldo1 is not limite1)

curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

print (curso is nome_curso)
print (curso is not nome_curso)
print (saldo is limite)
