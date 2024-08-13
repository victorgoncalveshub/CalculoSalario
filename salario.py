def calcular_inss(salario_bruto):
    faixas = [
        (1412.00, 0.075, 0),
        (2666.68, 0.09, 21.18),
        (4000.03, 0.12, 101.18),
        (7786.02, 0.14, 181.18)
    ]
    
    if salario_bruto <= faixas[0][0]:
        inss = salario_bruto * faixas[0][1]
    elif salario_bruto <= faixas[1][0]:
        inss = (salario_bruto * faixas[1][1]) - faixas[1][2]
    elif salario_bruto <= faixas[2][0]:
        inss = (salario_bruto * faixas[2][1]) - faixas[2][2]
    elif salario_bruto <= faixas[3][0]:
        inss = (salario_bruto * faixas[3][1]) - faixas[3][2]
    else:
        inss = (faixas[3][0] * faixas[3][1]) - faixas[3][2]
    
    return round(inss, 2)

def calcular_irrf(salario_liquido):
    faixas_ir = [
        (2259.20, 0.0, 0),
        (2826.65, 0.075, 169.44),
        (3751.05, 0.15, 381.44),
        (4664.68, 0.225, 662.77),
        (float('inf'), 0.275, 896.00)
    ]
    
    for faixa in faixas_ir:
        if salario_liquido <= faixa[0]:
            irrf_bruto = salario_liquido * faixa[1]
            irrf_liquido = irrf_bruto - faixa[2]
            return round(irrf_liquido, 2)

def calcular_descontos(salario_bruto, dependentes):
    inss = calcular_inss(salario_bruto)
    salario_liquido = salario_bruto - inss
    
    desconto_dependentes = dependentes * 189.59
    base_irrf = salario_liquido - desconto_dependentes
    
    if base_irrf > 0:
        irrf = calcular_irrf(base_irrf)
    else:
        irrf = 0.0
    
    return inss, irrf, salario_liquido - irrf

def calcular_salario_bruto(salario_liquido_desejado, dependentes):
    salario_bruto_estimado = salario_liquido_desejado * 1.4

    while True:
        inss, irrf, salario_liquido_calculado = calcular_descontos(salario_bruto_estimado, dependentes)
        
        if round(salario_liquido_calculado, 2) == round(salario_liquido_desejado, 2):
            return salario_bruto_estimado
        
        salario_bruto_estimado += (salario_liquido_desejado - salario_liquido_calculado) / 1.4

def calcular_custo_mei(salario_bruto):
    fgts = salario_bruto * 0.08
    inss_patronal = salario_bruto * 0.03
    decimo_terceiro = salario_bruto * 0.0925
    ferias = salario_bruto * 0.1233
    fgts_provisao = salario_bruto * 0.032
    
    custo_total = salario_bruto + fgts + inss_patronal + decimo_terceiro + ferias + fgts_provisao
    
    return {
        "Salário Bruto": round(salario_bruto, 2),
        "FGTS (8%)": round(fgts, 2),
        "INSS Patronal (3%)": round(inss_patronal, 2),
        "13º Salário + Encargos (9,25%)": round(decimo_terceiro, 2),
        "Férias + Encargos (12,33%)": round(ferias, 2),
        "FGTS Provisão (3,20%)": round(fgts_provisao, 2),
        "Custo Total": round(custo_total, 2)
    }

def calcular_custo_simples(salario_bruto):
    fgts = salario_bruto * 0.08
    fgts_provisao = salario_bruto * 0.04
    decimo_terceiro = salario_bruto * 0.0833
    ferias = salario_bruto * 0.1111
    previdenciario = salario_bruto * 0.0793
    
    custo_total = salario_bruto + fgts + fgts_provisao + decimo_terceiro + ferias + previdenciario
    
    return {
        "Salário Bruto": round(salario_bruto, 2),
        "FGTS (8%)": round(fgts, 2),
        "FGTS Provisão (4%)": round(fgts_provisao, 2),
        "13º Salário + Encargos (8,33%)": round(decimo_terceiro, 2),
        "Férias + Encargos (11,11%)": round(ferias, 2),
        "Previdenciário (7,93%)": round(previdenciario, 2),
        "Custo Total": round(custo_total, 2)
    }

def calcular_custo_lucro_real(salario_bruto):
    inss_patronal = salario_bruto * 0.20
    seguro_acidente = salario_bruto * 0.03
    salario_educacao = salario_bruto * 0.025
    decimo_terceiro = salario_bruto * 0.0833
    sistema_s = salario_bruto * 0.033
    ferias = salario_bruto * 0.1111
    
    custo_total = salario_bruto + inss_patronal + seguro_acidente + salario_educacao + decimo_terceiro + sistema_s + ferias
    
    return {
        "Salário Bruto": round(salario_bruto, 2),
        "INSS Patronal (20%)": round(inss_patronal, 2),
        "Seguro de Acidente de Trabalho (3%)": round(seguro_acidente, 2),
        "Salário-Educação (2,5%)": round(salario_educacao, 2),
        "13º Salário + Encargos (8,33%)": round(decimo_terceiro, 2),
        "Sistema 'S' (3,3%)": round(sistema_s, 2),
        "Férias + Encargos (11,11%)": round(ferias, 2),
        "Custo Total": round(custo_total, 2)
    }

def menu():
    while True:
        print("\nMenu Inicial:")
        print("1) Cálculo do salário líquido")
        print("2) Cálculo do salário bruto")
        print("3) Cálculo do Custo do Funcionário")
        print("4) Sair")
        
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            salario_bruto = float(input("Digite o salário bruto: R$ ").replace(',', '.'))
            dependentes = int(input("Digite o número de dependentes: "))
            inss, irrf, salario_final = calcular_descontos(salario_bruto, dependentes)
            print(f"Desconto do INSS: R$ {inss}")
            print(f"Desconto do IRRF: R$ {irrf}")
            print(f"Salário final (após descontos): R$ {salario_final}")

        elif opcao == '2':
            salario_liquido = float(input("Digite o salário líquido desejado: R$ ").replace(',', '.'))
            dependentes = int(input("Digite o número de dependentes: "))
            salario_bruto_necessario = calcular_salario_bruto(salario_liquido, dependentes)
            print(f"O salário bruto necessário para obter um salário líquido de R$ {salario_liquido} é: R$ {round(salario_bruto_necessario, 2)}")
        
        elif opcao == '3':
            print("Tipos de Empresa:")
            print("1) MEI")
            print("2) Simples")
            print("3) Lucro Presumido/Real")
            tipo_empresa = input("Escolha o tipo de empresa: ").strip()

            salario_bruto = float(input("Digite o salário do empregado: R$ ").replace(',', '.'))

            if tipo_empresa == '1':  # MEI
                custos = calcular_custo_mei(salario_bruto)
                print("\nCusto do Funcionário para a Empresa (MEI):")
                for item, valor in custos.items():
                    print(f"{item}: R$ {valor}")
            
            elif tipo_empresa == '2':  # Simples
                custos = calcular_custo_simples(salario_bruto)
                print("\nCusto do Funcionário para a Empresa (Simples):")
                for item, valor in custos.items():
                    print(f"{item}: R$ {valor}")
            
            elif tipo_empresa == '3':  # Lucro Presumido/Real
                custos = calcular_custo_lucro_real(salario_bruto)
                print("\nCusto do Funcionário para a Empresa (Lucro Presumido/Real):")
                for item, valor in custos.items():
                    print(f"{item}: R$ {valor}")
            
            else:
                print("Opção inválida. Escolha um tipo de empresa válido.")

        elif opcao == '4':
            print("Saindo do programa...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

# Executa o menu
menu()










