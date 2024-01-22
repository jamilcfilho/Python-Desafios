# Para as declarações de Variaveis e Constantes, utilizar nomes sugestivos e de forma SNAKE_CASE (utilizar _)

# Variáveis - Possuem valores que podem ser alterados

age = 23                          # Declarados de forma individual
name = 'Guilherme'                # Declarados de forma individual
print (f'Meu nome é {name} e eu tenho {age} ano(s) de idade.\n')

age, name = (27, 'Giovanna') # Podem ser declarados dessa forma também ou sem o '()' - Deixam código mais limpo
print (f'Meu nome é {name} e eu tenho {age} ano(s) de idade.\n')

age, name = 30, 'Jamil'
print (f'Meu nome é {name} e eu tenho {age} anos(s) de idade.\n\n')

limite_diario_saque = 1000
print (f"Limite diário de Saque no Banco central é de: {limite_diario_saque}\n\n")

# Constantes - Valores fixos que não alteram valor -> Porem Python não tem como declarar isso, por isso utiliza
# LETRAS MAIUSCULAS para diferencia-las e continua como regra mantendo o SNAKE_CASE

BRAZILIAN_STATES = "SP", "RJ", "BA", "RS"

print ('Estados Brasileiros que não alteram valores (constantes)')
print (BRAZILIAN_STATES)
