#             DESAFIO BÁSICO 2/3 - PYTHON DEVELOPER

# Leia um valor inteiro entre 1 e 12, inclusive.
# Correspondente a este valor, deve ser apresentado como resposta o mês do ano por extenso, em inglês,
# com a primeira letra em maiuscula.

# ENTRADA
# A entrada contém um único valor inteiro.

# SAÍDA
# Imprima por extenso o nome do mês correspondente ao número existente na estrada,
# com a primeira letra em maiuscula.
month = input()

months_dict = {"one": "January", "two": "February", "three": "March", "four": "April", "five": "May", "six": "June", "seven": "July", "eight": "August", "nine": "September", "ten": "October", "eleven": "November", "twelve": "December"}

while month != 0:
    if month == "1":
        print("{one}".format(**months_dict))

    elif month == "2":
        print("{two}".format(**months_dict))

    elif month == "3":
        print("{three}".format(**months_dict))

    elif month == "4":
        print("{four}".format(**months_dict))

    elif month == "5":
        print("{five}".format(**months_dict))

    elif month == "6":
        print("{six}".format(**months_dict))

    elif month == "7":
        print("{seven}".format(**months_dict))

    elif month == "8":
        print("{eight}".format(**months_dict))

    elif month == "9":
        print("{nine}".format(**months_dict))

    elif month == "10":
        print("{ten}".format(**months_dict))

    elif month == "11":
        print("{eleven}".format(**months_dict))

    elif month == "12":
        print("{twelve}".format(**months_dict))
    else:
        print ("Comando inválido!")
    break