# consumption_service.py
# Service para CALCULAR consumo de energia
# VERSÃO MUITO SIMPLES PARA INICIANTES

from repositories.user_appliance_repository import (
    get_user_appliances_by_user_id
)

from repositories.appliance_repository import (
    get_all_appliances
)

from repositories.consumption_repository import (
    get_all_consumption_levels
)


# FUNCAO 1: Calcula consumo de UM aparelho
def calcular_consumo_kwh(potencia, minutos_dia, dias_mes):

    # potencia = watts do aparelho
    # minutos_dia = minutos usados por dia
    # dias_mes = quantos dias usa no mes

    # Passo 1: Converte watts para kilowatts
    # (divide por 1000)
    kw = potencia / 1000

    # Passo 2: Calcula horas por dia
    # (divide minutos por 60 para virar horas)
    horas_dia = minutos_dia / 60

    # Passo 3: Calcula total de horas no mes
    # (multiplica horas por dia x dias)
    horas_mes = horas_dia * dias_mes

    # Passo 4: Consumo = kilowatts x horas
    consumo = kw * horas_mes

    # Retorna o consumo arredondado
    return round(consumo, 2)


# FUNCAO 2: Calcula consumo TOTAL do usuario
def calcular_consumo_usuario(id_usuario):

    # Busca aparelhos que este usuario tem
    aparelhos_usuario = get_user_appliances_by_user_id(id_usuario)

    # Busca info de TODOS os aparelhos
    todos_aparelhos = get_all_appliances()

    # Variavel para guardar o total
    consumo_total = 0

    # FOR = repetir para cada aparelho do usuario
    for aparelho_do_usuario in aparelhos_usuario:

        # FOR = procurar este aparelho na lista de todos
        for aparelho_info in todos_aparelhos:

            # IF = verifica se eh o mesmo aparelho
            if aparelho_info["id"] == aparelho_do_usuario["appliance_id"]:

                # Calcula consumo deste aparelho
                consumo = calcular_consumo_kwh(
                    aparelho_info["power"],
                    aparelho_do_usuario["daily_usage"],
                    aparelho_do_usuario["monthly_days"]
                )

                # Soma no total
                consumo_total = consumo_total + consumo

                # Para de procurar
                break

    # Retorna o consumo total
    return consumo_total


# FUNCAO 3: Busca niveis de consumo
def get_consumption_levels_service():
    return get_all_consumption_levels()


# FUNCAO 4: Calcula CUSTO em reais
def calcular_custo(consumo_kwh):

    # consumo_kwh = quanto de energia gastou

    # Preco por kWh (padrao brasileiro)
    preco = 0.95

    # Custo = consumo x preco
    custo = consumo_kwh * preco

    # Retorna arredondado
    return round(custo, 2)
