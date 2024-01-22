# IF = é uma condição de "Se" -> Só executada quando verdadeira, se não executa o ELSE
# IF / ELSE = é uma condição de "Se" e "Senão"
# IF / ELIF / ELSE = é uma condição de "Se", "Se não, se" e "Senão"

# ELIF é utilizado para testar mais condições, como por exemplo elaborar um Menu com opções numéricas e não deixar condição ir direto para o else e terminar o bloco
#não existe uma quantidade máxima de ELIFS, porém evitar criar grandes estruturas condicionais pois pode se perder nas condições e complica o código

# Estruturas condicionais permite um desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas


MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CHN.")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH.")


if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CHN.")
else:
    print("Ainda não pode tirar a CNH.")


if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CHN.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")
else:
    print("Ainda não pode tirar a CNH.")