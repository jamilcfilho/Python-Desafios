nome = "Guilherme"
idade = 28
profissao = "Progamador"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Guilherme", "idade": 28}  # Produção de um 'Dicionário'

print("Nome: %s Idade: %d" % (nome, idade))  #  Old Style %

print("Nome: {} Idade: {}".format(nome, idade))  #  format comum

print("Nome: {1} Idade: {0}".format(idade, nome))  # format colocando numeros e especificando a variável
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))

print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))  # format tendo como nomes entre as chaves {}
print("Nome: {name} Idade: {age} {name} {name} {age}".format(age=idade, name=nome)) # format com essa possibilidade de utilizar outro nome para a variável mas depois justifica elas certas
print("Nome: {nome} Idade: {idade}".format(**dados)) # Executar o dicionário

print(f"Nome: {nome} Idade: {idade}")  # f string - opcao mais utilizado hoje em dia por ja utilizar a variavel 
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")  # f string com indicação do saldo com 2 casas apos o float
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.1f}")  # f string com indicação de 10 espaços e depois 1 numero de casa após a virgula
