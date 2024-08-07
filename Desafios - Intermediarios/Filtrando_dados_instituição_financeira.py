#             DESAFIO INTERMEDIÁRIO - PYTHON DEVELOPER

#       Desafio
#   Você está consumindo dados de uma API de uma instituição financeira que fornece uma lista de transações.
# Seu desafio é filtrar todas as transações que possuem um valor acima de um determinado limite.

#       Entrada
#   A entrada deve receber dois valores:
#   1. Um número decimal representando o valor limite.
#   2. Uma string contendo transações no seguinte formato: "ID:VALOR;ID:VALOR;..."

#       Saída
#   Deverá retornar uma lista de strings, onde cada string contém as informações das transações cujo valor
# é maior que o valor limite especificado.


# Recebe o valor limite como entrada do usuário e converte para float
limite = float(input())
# Recebe a string de transações como entrada do usuário
transacoes = input()


# Define a função para filtrar transações acima do limite especificado
def filtrar_transacoes_acima_do_limite(limite, transacoes):
    if not transacoes:
        return []

    transacoes_filtradas = []
    lista_transacoes = transacoes.split(';')

    # Itera sobre cada transação na lista de transações
    for transacao in lista_transacoes:
        id_transacao, valor_str = transacao.split(':')
        valor = float(valor_str)

        # Compare o valor da transação com o limite e adiciona à lista filtrada se for maior
        if valor > limite:
            valor_formatado = f"{valor:.1f}" if valor.is_integer() else (
                '%.10g' % valor).rstrip('0').rstrip('.')
            transacao_formatada = f"{id_transacao}:{valor_formatado}"
            transacoes_filtradas.append(transacao_formatada)

    return transacoes_filtradas


# Imprime as transações com valores acima do limite
print(filtrar_transacoes_acima_do_limite(limite, transacoes))
