#             DESAFIO INTERMEDIÁRIO - PYTHON DEVELOPER

#       Desafio
#   O desafio consiste em implementar uma classe Calculadora que utilize os princípios da Programação
# Orientada a Objetos (POO). A classe deve conter um método para realizar a operação de 'soma' (somente)
# entre dois números inteiros, encapsulando assim a lógica matemática da adição.

#       Entrada
#   A entrada será composta por dois números inteiros fornecidos pelo usuário

#       Saída
#   A saída esperada é o resultado da soma dos dois números inteiros fornecidos como entrada

class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def soma(self):
        adicao = num1 + num2
        return adicao


# Entrada dos números pelo usuário
num1 = int(input())
num2 = int(input())

# Criando uma instância da calculadora
calc = Calculadora(num1, num2)

resultado = calc.soma()
print(resultado)
