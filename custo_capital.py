def calcular_custo_oportunidade():
    taxa_desc = float(input("Digite a taxa de desconto: "))
    fluxo_caixa = float(input("Digite o valor do fluxo de caixa: "))
    taxa_min_atratividade = float(input("Digite a taxa mínima de atratividade: "))
    
    custo_oportunidade = fluxo_caixa / (1 + taxa_min_atratividade) ** taxa_desc
    
    print(f"O custo de oportunidade é: {custo_oportunidade:.2f}")
    print(f"Isso representa o valor atualizado do fluxo de caixa descontado pela taxa de atratividade e depreciação da moeda.")

def calcular_custo_capital_proprio():
    taxa_min_atratividade = float(input("Digite a taxa mínima de atratividade: "))
    taxa_juros_atual = float(input("Digite a taxa de juros atual (ex: 0.06 para 6%): "))
    
    custo_capital_proprio = taxa_min_atratividade
    comparativo = custo_capital_proprio - taxa_juros_atual
    
    print(f"O custo de capital próprio é: {custo_capital_proprio:.2%}")
    print(f"Isso representa a taxa mínima de atratividade desejada para o investimento. O comparativo com a taxa de juros atual mostra a diferença entre a atratividade desejada e a realidade atual.")

def calcular_custo_capital_terceiros():
    juros = float(input("Digite o valor dos juros anuais: "))
    capital_terceiros = float(input("Digite o valor do capital de terceiros (sem considerar passivos circulantes): "))
    
    custo_capital_terceiros = juros / capital_terceiros
    
    print(f"O custo de capital de terceiros é: {custo_capital_terceiros:.2%}")
    print("Isso representa a taxa de juros anuais pagos em relação ao capital de terceiros.")
    
def calcular_wacc():
    custo_capital_terceiros = float(input("Digite o custo de capital de terceiros (ex: 0.08 para 8%): "))
    custo_capital_proprio = float(input("Digite o custo de capital próprio (ex: 0.10 para 10%): "))
    participacao_terceiros = float(input("Digite a participação do capital de terceiros no passivo total (ex: 0.4 para 40%): "))
    participacao_proprio = 1 - participacao_terceiros
    
    wacc = (custo_capital_terceiros * participacao_terceiros) + (custo_capital_proprio * participacao_proprio)
    
    print(f"O WACC (Custo Médio Ponderado de Capital) é: {wacc:.2%}")
    print("Isso representa a média ponderada dos custos de capital de terceiros e próprio, considerando suas respectivas participações no passivo total.")

def main():
    print("Escolha a opção:")
    print("1. Calcular Custo de Oportunidade")
    print("2. Calcular Custo de Capital Próprio")
    print("3. Calcular Custo de Capital de Terceiros")
    print("4. Calcular WACC (Custo Médio Ponderado de Capital)")
    
    opcao = int(input())
    
    if opcao == 1:
        calcular_custo_oportunidade()
    elif opcao == 2:
        calcular_custo_capital_proprio()
    elif opcao == 3:
        calcular_custo_capital_terceiros()
    elif opcao == 4:
        calcular_wacc()
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    main()