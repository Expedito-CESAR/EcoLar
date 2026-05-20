# energy_classification_service.py
# Service para CLASSIFICAR consumo de energia
# VERSAO MUITO SIMPLES COM IF/ELIF/ELSE

from services.consumption_service import (
    calcular_consumo_usuario,
    calcular_custo
)


# FUNCAO: Classifica consumo do usuario
def classificar_consumo(id_usuario):

    # Calcula consumo total
    consumo = calcular_consumo_usuario(id_usuario)

    # Variavel para guardar a classificacao
    classificacao = ""

    # IF/ELIF/ELSE = estrutura de decisao

    # IF 1: Verifica se consumo eh muito baixo
    if consumo <= 50:

        classificacao = "MUITO BAIXO"

    # ELIF 2: Verifica se consumo eh baixo
    elif consumo <= 100:

        classificacao = "BAIXO"

    # ELIF 3: Verifica se consumo eh medio
    elif consumo <= 150:

        classificacao = "MEDIO"

    # ELIF 4: Verifica se consumo eh alto
    elif consumo <= 250:

        classificacao = "ALTO"

    # ELSE: Consumo eh muito alto
    else:

        classificacao = "MUITO ALTO"

    # Retorna a classificacao
    return {
        "consumo_kwh": consumo,
        "classificacao": classificacao
    }


# FUNCAO: Compara consumo com media nacional
def comparar_com_media(id_usuario):

    # Calcula consumo do usuario
    consumo_usuario = calcular_consumo_usuario(id_usuario)

    # Media nacional eh 150 kWh por mes
    media_nacional = 150

    # Variavel para resultado
    status = ""

    # IF: Verifica se usuario consome MAIS que media
    if consumo_usuario > media_nacional:

        status = "ACIMA"

    # ELIF: Verifica se consome IGUAL a media
    elif consumo_usuario == media_nacional:

        status = "IGUAL"

    # ELSE: Consome MENOS que media
    else:

        status = "ABAIXO"

    # Retorna resultado
    return {
        "consumo_usuario_kwh": consumo_usuario,
        "media_nacional_kwh": media_nacional,
        "status": status
    }


# FUNCAO: Classifica por faixa de consumo
def classificar_por_faixa(id_usuario):

    # Calcula consumo
    consumo = calcular_consumo_usuario(id_usuario)

    # Variavel para guardar faixa
    faixa = ""

    # IF/ELIF/ELSE para classificar em FAIXAS

    # Faixa 1: Consumo muito baixo (0-30 kWh)
    if consumo < 30:

        faixa = "FAIXA 1: Minimo (0-30 kWh)"

    # Faixa 2: Consumo baixo (30-60 kWh)
    elif consumo < 60:

        faixa = "FAIXA 2: Baixo (30-60 kWh)"

    # Faixa 3: Consumo medio (60-100 kWh)
    elif consumo < 100:

        faixa = "FAIXA 3: Medio (60-100 kWh)"

    # Faixa 4: Consumo alto (100-150 kWh)
    elif consumo < 150:

        faixa = "FAIXA 4: Alto (100-150 kWh)"

    # Faixa 5: Consumo muito alto (150+ kWh)
    else:

        faixa = "FAIXA 5: Muito Alto (150+ kWh)"

    # Retorna faixa
    return faixa
