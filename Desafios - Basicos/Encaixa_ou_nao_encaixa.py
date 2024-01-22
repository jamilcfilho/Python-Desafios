#             DESAFIO BÁSICO 3/3 - PYTHON DEVELOPER

# Paulinho tem em suas mãos um novo problema.
# Agora a sua professora lhe pediu que construísse um programa para verificar,
# à partir de dois valores muito grandes A e B, se B corresponde aos últimos dígitos de A.

# ENTRADA
# A entrada consiste de vários casos de teste.
# A primeira linha de entrada contém um inteiro N que indica a quantidade de casos de teste.
# Cada caso de teste consiste de dois valores A e B maiores que zero, cada um deles podendo ter até 1000 dígitos.

# SAÍDA
# Para cada caso de entrada imprima uma mensagem indicando se o segundo valor encaixa no 
# primeiro valor, confome exemplo abaixo.

# NÃO UTILIZAR PARA PODER ENTENDER E FAZER UM CÓDIGO MELHOR AINDA

qt = int(input())

v = []



for i in range(qt):

  v = input().split(" ")

  a = v[0]

  b = v[1]



  if len(b) > len(a):

    print("nao encaixa")

  elif a.endswith(b):

    print("encaixa")

  else:

    print("nao encaixa")  