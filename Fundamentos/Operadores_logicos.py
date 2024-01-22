# AND = para ser True "TUDO" tem que ser True        -> and = 'E'
# OR = para ser True "APENAS UM" tem que ser True    -> or = 'OU'

# NOT = operadore de 'NEGAÇÃO' -> NOT é o inverso da lógica -> NOT de False = True e vice versa

print(True and True and True)     # Verdade
print(True and False and True)    # Falso
print(False and False and False)  # Falso
print(True or True or True)       # Verdade
print(True or False or False)     # Verdade
print(False or False or False)    # Falso

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque) # Parenteses para indicar quem executa 1º
print(exp_2)

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite   # Deixar o código mais legivel, compensa e
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque # muito colocar em variáveis Logicas grandes
                                                                        # isso que foi feito no

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)

not 1000 > 1500  # NOT é o inverso da afirmação, então 1000 é menor 1500 (true) porem com o NOT vira False

contatos_emergencia = []  # É uma lista, só que lista vazia em Python é igual a FALSE

print (not contatos_emergencia)

print (not "saque 1500")

print (not"")