#           Desafio Avançado

#       INTRODUÇÃO
#   Em nossa aplicação financeira, identificamos a necessidade de rastrear e auditar as ações dos usuários para
# garantir a segurança e a integridade das operações. O console tem sido útil até agora, mas a quantidade crescente
# de atividades torna difícil acompanhar todas as operações em tempo real. Portanto, decidimos que é vital
# registrar essas informações em um arquivo para análise posterior e backup contínuo.

#       OBJETIVO GERAL
#   Modificar o atual decorador de log, que imprime informações no console, para que ele salve essas informações
# em um arquivo de log, possibilitando uma revisão mais fácil e uma análise mais detalhada das operações
# dos usuários.

#       DESAFIO
#   O decorador deve registrar o seguinte para cada chamada de função:
# 1 - Data e hora atuais
# 2 - Nome da função
# 3 - Argumentos da função
# 4 - Valor retornado pela função
# 5 - O arquivo de log deve ser chamado log.txt.
# 6 - Se o arquivo log.txt já existir, os novos logs devem ser adicionados ao final do arquivo.
# 7 - Cada entrada de log deve estar em uma nova linha.

from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime
from pathlib import Path

ROOT_PATH = Path(__file__).parent


class ContasIterador:
    def __init__(self, contas):
        self.contas = contas
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            conta = self.contas[self.index]
            return f"""\
            Agência:\t{conta.agencia}
            Número:\t{conta.numero}
            Titular:\t{conta.cliente.nome}
            Saldo:\tR$ {conta.saldo:.2f}
        """
        except IndexError:
            raise StopIteration
        finally:
            self.index += 1


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
        self.indice_conta = 0

    def realizar_transacao(self, conta, transacao):
        if len(conta.historico.transacoes_do_dia()) >= 2:
            print("\n-- Você excedeu o número de transações permitidas! --")
            return

        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: ('{self.nome}', '{self.cpf}')>"


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

    @classmethod
    def nova_conta(cls, cliente, numero, limite, limite_saques):
        return cls(numero, cliente, limite, limite_saques)

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

    def __repr__(self):
        return f"<{self.__class__.__name__}: ('{self.agencia}', '{self.numero}', '{self.cliente.nome}')>"

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

    def gerar_relatorio(self, tipo_transacao=None):
        for transacao in self._transacoes:
            if tipo_transacao is None or transacao["tipo"].lower() == tipo_transacao.lower():
                yield transacao

    def transacoes_do_dia(self):
        data_atual = datetime.utcnow().date()
        transacoes = []
        for transacao in self._transacoes:
            data_transacao = datetime.strptime(
                transacao["data"], "%d-%m-%Y %H:%M:%S").date()
            if data_atual == data_transacao:
                transacoes.append(transacao)
        return transacoes


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


def log_transacao(func):
    def envelope(*args, **kwargs):
        resultado = func(*args, **kwargs)
        data_hora = datetime.utcnow().strftime("%d-%m-%Y %H:%M:%S")
        with open(ROOT_PATH / "log.txt", "a") as arquivo:
            arquivo.write(f"[{data_hora}] | Função '{func.__name__}' executada com argumentos {args} e {kwargs}."
                          f"Retornou {resultado}\n")
        return resultado

    return envelope


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


@log_transacao
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


@log_transacao
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


@log_transacao
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
    extrato = ""
    tem_transacao = False
    for transacao in conta.historico.gerar_relatorio():
        tem_transacao = True
        extrato += f"\n{transacao['tipo']}:\tR$ {transacao['valor']:.2f}"

    if not tem_transacao:
        extrato = "Não foram realizadas movimentações."

    print(extrato)
    print("-" * 41)
    print(f"\nSaldo:\tR$ {conta.saldo:.2f}")
    print("#########################################")


@log_transacao
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


@log_transacao
def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n-- Cliente não encontrado, fluxo de criação de conta encerrado! --")
        return

    conta = ContaCorrente.nova_conta(
        cliente=cliente, numero=numero_conta, limite=500, limite_saques=50)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n-- Conta criada com sucesso! --")


def listar_contas(contas):
    for conta in ContasIterador(contas):
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
