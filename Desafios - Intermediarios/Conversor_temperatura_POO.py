#             DESAFIO INTERMEDIÁRIO - PYTHON DEVELOPER

#       Desafio

#   Implemente uma classe ConversorTemperatura que converte temperaturas de Celsius para Fahrenheit. A classe
# deve incluir um método chamado celsius_para_fahrenheit que realiza o cálculo de conversão. A fórmula para
# converter de Celsius para Fahrenheit é:
#           Fahrenheit=(Celsius×95)+32Fahrenheit=(Celsius×59​)+32
#   Você também deverá criar uma instância do conversor e utilizar essa instância para realizar a conversão.

#       Entrada
#   O programa deverá receber como entrada uma temperatura em graus Celsius fornecida pelo usuário.

#       Saída
#   O programa deverá exibir a temperatura convertida para Fahrenheit.

class ConversorTemperatura:
    def __init__(self, celsius):
        self.celsius = celsius

    def celsius_para_fahrenheit(self):
        # Fórmula de conversão de Celsius para Fahrenheit
        fahrenheit = (celsius * 9 / 5) + 32
        return fahrenheit


# Entrada do usuário
celsius = float(input())

# Criando uma instância do conversor:
conversor = ConversorTemperatura(celsius)

# Chamando o método e imprimir o resultado:
fahrenheit = conversor.celsius_para_fahrenheit()
print(fahrenheit)
