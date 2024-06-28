#           Desafio Intermediário

# João tem uma bicicletaria e gostaria de registrar suas bicicletas.
# Crie um prgrama através da Programação Orientada a Objetos onde João informa: cor, modelo, ano e valor da bicicleta (atributos).
# Uma bicicleta pode: buzinar, parar e correr. Adicione esses comportamentos (métodos).

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Parando a bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vruuuuum...")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave,valor in self.__dict__.items()])}"

bicicleta1 = Bicicleta("preta", "caloi", "2023", 990)

print(bicicleta1.cor, bicicleta1.modelo, bicicleta1.ano, bicicleta1.valor) # Formato de imprimir o objeto, porém de forma mais trabalhosa e se caso alterar algum atributo, precisa vir nessa parte do código e alterar
bicicleta1.buzinar()
bicicleta1.correr()
bicicleta1.parar()

# ou (mesma coisa só que deixa o código mais "complexo")

Bicicleta.buzinar(bicicleta1)
Bicicleta.correr(bicicleta1)
Bicicleta.parar(bicicleta1)

print("=" * 40)

bicicleta2 = Bicicleta("Verde", "Monark", "2024", 350)

print(bicicleta2) # Através do def __str__ e do seu return, qualquer atributo que for adicionado a classe, automaticamente já será incluído para impressão da classe e seus atributos

bicicleta2.buzinar()
bicicleta2.correr()
bicicleta2.parar()