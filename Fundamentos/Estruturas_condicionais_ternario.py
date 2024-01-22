# IF TERNARIO -> Permite escrever uma condição em uma única linha. Composto por 3 partes: 1-Retorno caso expressão seja verdadeira
#2-É a expressão lógica e 3-Retorno caso a expressão não seja atendida

#Primeira parte vem antes do IF | Segunda parte entre o IF e o ELSE dando uma condição | Terceira parte é após o ELSE que é o que será exibido

saldo = 2000
saque = 2500

status = "Sucesso" if saldo >= saque else "Falha"
#         1 parte  ||  2 parte        ||  3 parte
print(f"{status} ao realizar o saque!")