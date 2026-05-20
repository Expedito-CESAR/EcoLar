# simulation_service.py
# Service para SIMULAR economia de energia
# VERSAO MUITO SIMPLES COM CONTAS BASICAS

from services.consumption_service import (
    calcular_consumo_usuario,
    calcular_custo
)


# FUNCAO: Simula economia se reduzir consumo
def simular_economia(id_usuario, percentual_reducao):

    # id_usuario = ID do usuario
    # percentual_reducao = quanto % vai reduzir (ex: 30 para 30%)

    # Calcula consumo ATUAL
    consumo_atual = calcular_consumo_usuario(id_usuario)

    # Calcula custo ATUAL
    custo_atual = calcular_custo(consumo_atual)

    # Calcula novo consumo REDUZIDO
    # Formula: novo_consumo = atual - (atual * percentual / 100)
    reducao_em_kwh = consumo_atual * percentual_reducao / 100
    consumo_novo = consumo_atual - reducao_em_kwh

    # Calcula custo NOVO
    custo_novo = calcular_custo(consumo_novo)

    # Calcula economia em REAIS
    economia_reais = custo_atual - custo_novo

    # Calcula economia em um ANO
    economia_ano = economia_reais * 12

    # Retorna tudo
    return {
        "consumo_atual_kwh": consumo_atual,
        "custo_atual_reais": custo_atual,
        "percentual_reducao": percentual_reducao,
        "consumo_novo_kwh": round(consumo_novo, 2),
        "custo_novo_reais": custo_novo,
        "economia_mensal_reais": round(economia_reais, 2),
        "economia_anual_reais": round(economia_ano, 2)
    }


# FUNCAO: Simula economia com 3 opcoes
def simular_multiplas_reducoes(id_usuario):

    # Calcula consumo atual
    consumo_atual = calcular_consumo_usuario(id_usuario)
    custo_atual = calcular_custo(consumo_atual)

    # SIMULACAO 1: Reduzir 10%
    reducao_10 = consumo_atual * 10 / 100
    consumo_10 = consumo_atual - reducao_10
    custo_10 = calcular_custo(consumo_10)
    economia_10 = custo_atual - custo_10

    # SIMULACAO 2: Reduzir 20%
    reducao_20 = consumo_atual * 20 / 100
    consumo_20 = consumo_atual - reducao_20
    custo_20 = calcular_custo(consumo_20)
    economia_20 = custo_atual - custo_20

    # SIMULACAO 3: Reduzir 30%
    reducao_30 = consumo_atual * 30 / 100
    consumo_30 = consumo_atual - reducao_30
    custo_30 = calcular_custo(consumo_30)
    economia_30 = custo_atual - custo_30

    # Retorna as 3 simulacoes
    return {
        "consumo_atual": consumo_atual,
        "custo_atual": custo_atual,
        "opcao_10_porcento": {
            "percentual": 10,
            "novo_consumo": round(consumo_10, 2),
            "novo_custo": custo_10,
            "economia_mensal": round(economia_10, 2),
            "economia_anual": round(economia_10 * 12, 2)
        },
        "opcao_20_porcento": {
            "percentual": 20,
            "novo_consumo": round(consumo_20, 2),
            "novo_custo": custo_20,
            "economia_mensal": round(economia_20, 2),
            "economia_anual": round(economia_20 * 12, 2)
        },
        "opcao_30_porcento": {
            "percentual": 30,
            "novo_consumo": round(consumo_30, 2),
            "novo_custo": custo_30,
            "economia_mensal": round(economia_30, 2),
            "economia_anual": round(economia_30 * 12, 2)
        }
    }
