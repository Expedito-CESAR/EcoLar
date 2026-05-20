# energy_simple_controller.py
# Controller MUITO SIMPLES para exibir energia
# So usa if/else/print

from services.consumption_service import (
    calcular_consumo_usuario,
    calcular_custo
)

from services.energy_classification_service import (
    classificar_consumo,
    comparar_com_media,
    classificar_por_faixa
)

from services.simulation_service import (
    simular_economia,
    simular_multiplas_reducoes
)


# FUNCAO 1: Mostra consumo simples
def mostrar_consumo_simples(usuario):

    print("\n===== CONSUMO DE ENERGIA =====\n")

    # Calcula consumo
    consumo = calcular_consumo_usuario(usuario["id"])

    # Calcula custo
    custo = calcular_custo(consumo)

    # Exibe
    print(f"Consumo mensal: {consumo} kWh")
    print(f"Custo mensal: R$ {custo}")


# FUNCAO 2: Mostra classificacao
def mostrar_classificacao(usuario):

    print("\n===== CLASSIFICACAO ENERGETICA =====\n")

    # Classifica
    dados = classificar_consumo(usuario["id"])

    # Exibe
    print(f"Consumo: {dados['consumo_kwh']} kWh")
    print(f"Classificacao: {dados['classificacao']}")

    # Exibe comparacao com media
    comparacao = comparar_com_media(usuario["id"])

    print(f"\nComparacao com media nacional:")
    print(f"Media nacional: {comparacao['media_nacional_kwh']} kWh")
    print(f"Seu consumo: {comparacao['status']} da media")

    # Exibe faixa
    faixa = classificar_por_faixa(usuario["id"])
    print(f"\nFaixa: {faixa}")


# FUNCAO 3: Mostra economia simples
def mostrar_economia_simples(usuario):

    print("\n===== ECONOMIA POTENCIAL =====\n")

    # Simula 30% de reducao
    economia = simular_economia(usuario["id"], 30)

    print(f"Consumo atual: {economia['consumo_atual_kwh']} kWh")
    print(f"Custo atual: R$ {economia['custo_atual_reais']}")

    print(f"\nSe reduzir {economia['percentual_reducao']}%:")
    print(f"Novo consumo: {economia['consumo_novo_kwh']} kWh")
    print(f"Novo custo: R$ {economia['custo_novo_reais']}")

    print(f"\nEconomia:")
    print(f"Por mes: R$ {economia['economia_mensal_reais']}")
    print(f"Por ano: R$ {economia['economia_anual_reais']}")


# FUNCAO 4: Mostra multiplas opcoes
def mostrar_opcoes_economia(usuario):

    print("\n===== OPCOES DE ECONOMIA =====\n")

    # Simula 3 opcoes
    dados = simular_multiplas_reducoes(usuario["id"])

    print(f"Consumo atual: {dados['consumo_atual']} kWh (R$ {dados['custo_atual']})")
    print("\n--- OPCAO 1: Reduzir 10% ---")
    opt1 = dados["opcao_10_porcento"]
    print(f"Novo consumo: {opt1['novo_consumo']} kWh")
    print(f"Economia mensal: R$ {opt1['economia_mensal']}")
    print(f"Economia anual: R$ {opt1['economia_anual']}")

    print("\n--- OPCAO 2: Reduzir 20% ---")
    opt2 = dados["opcao_20_porcento"]
    print(f"Novo consumo: {opt2['novo_consumo']} kWh")
    print(f"Economia mensal: R$ {opt2['economia_mensal']}")
    print(f"Economia anual: R$ {opt2['economia_anual']}")

    print("\n--- OPCAO 3: Reduzir 30% ---")
    opt3 = dados["opcao_30_porcento"]
    print(f"Novo consumo: {opt3['novo_consumo']} kWh")
    print(f"Economia mensal: R$ {opt3['economia_mensal']}")
    print(f"Economia anual: R$ {opt3['economia_anual']}")
