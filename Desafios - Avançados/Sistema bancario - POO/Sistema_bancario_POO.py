#           Desafio Intermediário

#       OBJETIVO GERAL
#   Iniciar a modelagem do sistema bancário em Programação Orientada a Objetos.
#   Adicionar classes para cliente e as operações bancárias: depósito e saque.

#       DESAFIO
#   Implementar um sistema bancário em POO, que armazene os dados dos clientes
# e contas bancárias em objetos ao invés de dicionários.
#   O código deve seguir o modelo de classes UML disponível.
#   Após concluir a modelagem das classes e a criação dos métodos, atualize os métodos que tratam das opções
# de um menu para funcionarem com as classes modeladas.

from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self._saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print(
                "\n-- Não foi possível realizar o saque! Você não possui saldo suficiente. --")

        elif valor > 0:
            self._saldo -= valor
            print("\n-- Saque realizado com sucesso! --")
            return True

        else:
            print("\n-- Operação falhou! O valor informado é inválido. --")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n-- Depósito realizado com sucesso! --")

        else:
            print("\n-- Operação falhou! O valor informado é inválido. --")
            return False

        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"]
                == Saque.__name__]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print(
                "\nLimite de saque por operação é de R$ 500,00.\n\tPor favor repetir o processo!"
            )

        elif excedeu_saques:
            print("Você excedeu o número máximo de 3 saques diários")

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )


class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


def menu():

    menu = """\n
    ####################################
    Digite a opção desejada da operação:

    [1] Depositar 
    [2] Sacar
    [3] Extrato
    [4] Novo usuário
    [5] Nova conta
    [6] Listar contas
    [0] Sair
    ####################################
    => """
    return input(menu)


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [
        cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n-- Cliente não possui conta! --")
        return

    # FIXME: não permite cliente escolher conta --> Isso aqui posso melhorar no futuro adicionando opções de escolher contas do cliente, afinal 1 cliente pode possui várias contas
    return cliente.contas[0]


def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n-- Cliente não encontrado! --")
        return

    valor = float(input("Informe o valor a ser depositado: R$ "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n-- Cliente não encontrado! --")
        return

    valor = float(input("Informe o valor do saque: R$ "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n-- Cliente não encontrado! --")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n################ Extrato ################\n")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."

    else:
        for transacoes in transacoes:
            extrato += f"\n{transacoes['tipo']}:\tR$ {transacoes['valor']:.2f}"

    print(extrato)
    print("-" * 41)
    print(f"\nSaldo:\tR$ {conta.saldo:.2f}")
    print("#########################################")


def criar_clientes(clientes):
    cpf = input("Informe o CPF (somente números): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n-- Já existe cadastro de cliente com esse número de CPF! --")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input(
        "informe o endereço (logradouro, nº - bairro - cidade/sigla do estado): ")

    cliente = PessoaFisica(
        nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print("\n-- Cliente cadastrado com sucesso! --")


def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n-- Cliente não encontrado, fluxo de criação de conta encerrado! --")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n-- Conta criada com sucesso! --")


def listar_contas(contas):
    for conta in contas:
        print("=" * 50)
        print(str(conta))


def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            depositar(clientes)

        elif opcao == "2":
            sacar(clientes)

        elif opcao == "3":
            exibir_extrato(clientes)

        elif opcao == "4":
            criar_clientes(clientes)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            break

        else:
            print(
                "\n-- Operação inválida! Por favor selecione novamente o número da operação desejada! --")


main()