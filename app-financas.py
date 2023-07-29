#código de app para entender e facilitar a vida financeira de forma simples, por Lucas Caracik
def pedir_despesa():
    nome_despesa = input("Nomeie uma despesa mensal:")
    valor_despesa = float(input("Digite o valor em reais da despesa {}: ".format(nome_despesa)))
    return nome_despesa, valor_despesa

#Dicionário para armazenar as despesas

despesas_mensais = {}

#Pedir nome e valor de cada despesa e armazenar no dicionário

while True:
    nome_despesa, valor_despesa = pedir_despesa()
    despesas_mensais[nome_despesa] = valor_despesa

    continuar = input("Deseja adicionar mais uma despesa? (s/n): ")
    if continuar.lower() != 's':
        break

def pedir_recebimento():
    nome_recebimento = input("Nomeie um recebimento mensal:")
    valor_recebimento = float(input("Digite o valor em reais do recebimento {}: ".format(nome_recebimento)))
    return nome_recebimento, valor_recebimento

#Dicionário para armazenar os recebimentos

recebimentos_mensais = {}

#Pedir nome e valor de cada recebimento e armazenar no dicionário

while True:
    nome_recebimento, valor_recebimento = pedir_recebimento()
    recebimentos_mensais[nome_recebimento] = valor_recebimento

    continuar = input("Deseja adicionar mais um recebimento? (s/n): ")
    if continuar.lower() != 's':
        break

def calcular_despesas_totais(total_despesas):
    total_despesas = sum(despesas_mensais.values())
    return total_despesas

def calcular_recebimentos_totais(total_recebimentos):
    total_recebimentos = sum(recebimentos_mensais.values())
    return total_recebimentos

def calcular_balanco(total_recebimentos, total_despesas):
    balanco_total = total_recebimentos - total_despesas
    return balanco_total

#Solicitar o quanto a pessoa quer poupar/guardar mensalmente

def pedir_valor_poupanca(balanco_total):
        valor_poupanca = float(input("Digite o valor que você gostaria de poupar mensalmente em reais: "))
        if valor_poupanca <= balanco_total:
            return valor_poupanca
        else:
            print("O valor de poupança é maior que o disponível. Por favor, insira um valor menor: ")

#Definir o limite recomendável do cartão de crédito

def limite_cartao_credito(balanco_total, valor_poupanca):
    limite_cartao = balanco_total - valor_poupanca
    return limite_cartao

# desenvolver print(limite_cartao)


#não usado

# #Exibir as despesas cadastradas
# print("\nDespesas cadastradas:")
# for despesa, valor in despesas_mensais.items():
#     print("{}: R$ {:.2f}".format(despesa, valor))
#
# #Exibir os recebimentos cadastrados
# print("\nRecebimentos cadastrados:")
# for recebimento, valor in recebimentos_mensais.items():
#     print("{}: R$ {:.2f}".format(recebimento, valor))