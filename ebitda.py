def calcular_ebitda(receita, despesas_operacionais, depreciacao, amortizacao):
    ebitda = receita - despesas_operacionais + depreciacao + amortizacao
    return ebitda

# Entrada fornecida pelo usuário
receita = float(input("Digite a receita total: "))
despesas_operacionais = float(input("Digite as despesas operacionais: "))
depreciacao = float(input("Digite a despesa de depreciação: "))
amortizacao = float(input("Digite a despesa de amortização: "))

resultado_ebitda = calcular_ebitda(receita, despesas_operacionais, depreciacao, amortizacao)

# Cálculo da margem EBITDA
margem_ebitda = (resultado_ebitda / receita) * 100

print("EBITDA:", resultado_ebitda)
print("Margem EBITDA:", margem_ebitda, "%")

# Observação sobre a margem EBITDA
if margem_ebitda > 0:
    print("A margem EBITDA é positiva.")
elif margem_ebitda < 0:
    print("A margem EBITDA é negativa.")
else:
    print("A margem EBITDA é neutra.")