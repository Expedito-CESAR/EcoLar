# user_appliance_service.py

# from = usado para importar partes específicas de outro arquivo
# import = traz funções/classes/módulos para este arquivo

# Importa função responsável por salvar aparelhos do usuário
# repositories = camada responsável por acessar arquivos TXT/dados
from repositories.user_appliance_repository import (
    create_user_appliance_repository,
    update_user_appliance_repository,
    delete_user_appliance_repository,
    delete_user_appliances_by_user_id
)

# Importa as funções de validação
from utils.validators import (
    # Valida números positivos
    validate_positive_number,
    # Valida IDs
    validate_id
)

# def = usado para criar funções

# create_user_appliance_service = função responsável por organizar
# dados antes de enviar ao repository

def create_user_appliance_service(

        # ID do usuário
        user_id,

        # ID do aparelho
        appliance_id,

        # Tempo médio diário de uso
        daily_usage,

        # Quantidade de dias no mês
        monthly_days
):

    # Verifica se ID do aparelho é válido
    if not validate_id(appliance_id):
        # retorna mensagem de erro
        return "ID inválido."
    # Verifica se tempo diário é positivo
    if not validate_positive_number(daily_usage):
        # retorna erro
        return "Uso diário inválido."
    # Verifica se dias mensais são positivos
    if not validate_positive_number(monthly_days):
        # retorna erro
        return "Dias inválidos."
        
    # Cria dicionário com dados do aparelho do usuário
    # dict = estrutura chave:valor
    user_appliance = {

        # ID do usuário
        "user_id": user_id,

        # ID do aparelho
        "appliance_id": appliance_id,

        # Converte valores para inteiro
        # antes da persistência
        "daily_usage": int(daily_usage),

        "monthly_days": int(monthly_days)
    }


    # Chama repository responsável por salvar no TXT
    create_user_appliance_repository(user_appliance)

    # Atualiza aparelho vinculado ao usuário

def update_user_appliance_service(
    updated_appliance
):

    return update_user_appliance_repository(
        updated_appliance
    )


# Remove aparelho específico do usuário

def delete_user_appliance_service(
    user_id,
    appliance_id
):

    return delete_user_appliance_repository(
        user_id,
        appliance_id
    )


# Remove todos os aparelhos vinculados ao usuário

def delete_all_user_appliances_service(
    user_id
):

    return delete_user_appliances_by_user_id(
        user_id
    )