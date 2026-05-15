# from = usado para importar partes específicas de outro arquivo
# import = traz funções/classes/módulos para este arquivo

# Importa funções do arquivo user_service.py
from services.user_service import (
    # Função responsável por criar usuário
    create_user_service,
    # Função responsável pelo login
    login_user_service
)

# Importa função relacionada aos aparelhos do usuário
from services.user_appliance_service import (
    # Serviço responsável por cadastrar aparelhos do usuário
    create_user_appliance_service
    )

# Importa função do repository de aparelhos
# repositories = camada responsável por acessar arquivos TXT/dados
from repositories.appliance_repository import (
    # Função que retorna todos os aparelhos cadastrados
    get_all_appliances
)

# Importa repository dos níveis de consumo
from repositories.consumption_repository import (
    # Função que retorna todos os níveis de consumo
    get_all_consumption_levels
)


# Importa funções da view do usuário
# views = camada responsável pela interação visual com o terminal
from views.user_view import (
    # Mostra título do cadastro
    show_user_registration_title,
    # Captura nome digitado pelo usuário
    get_user_name,
    # Captura e-mail digitado
    get_user_email,
    # Captura data de nascimento
    get_user_birthday,
    # Exibe mensagem de erro
    show_error,
    # Exibe mensagem de sucesso
    show_success
)

# Importa função da view de aparelhos
from views.appliance_view import show_appliance

# Importa função da view de consumo
from views.consumption_view import show_consumption_levels

# Importa funções de validação
# validators = arquivo responsável por validar entradas do usuário
from utils.validators import (
    # Verifica se número é positivo
    validate_positive_number,
    # Verifica se ID é válido
    validate_id,
    # Verifica se opção do menu existe
    validate_menu_option
)

# def = usado para criar funções
# create_user_controller = função responsável pelo fluxo de cadastro
def create_user_controller():
    # Exibe título do cadastro
    show_user_registration_title()
    # Recebe nome do usuário
    name = get_user_name()
    # Recebe e-mail
    email = get_user_email()
    # Recebe data de aniversário
    birthday = get_user_birthday()
    # Busca níveis de consumo no repository
    levels = get_all_consumption_levels()
    # Exibe níveis disponíveis
    show_consumption_levels(levels)
    # input() = captura texto digitado no terminal
    profile = input("\nEscolha o ID do perfil: ")
    # Chama service de criação do usuário
    # user recebe dados do usuário
    # error recebe mensagem de erro caso exista
    user, error = create_user_service(
        name,
        email,
        birthday,
        profile
    )
    # if = estrutura condicional
    # Verifica se houve erro
    if error:
        # Exibe erro na tela
        show_error(error)
        # return = encerra função atual
        return


    # busca aparelhos cadastrados
    appliances = get_all_appliances()
    # exibe aparelhos disponíveis
    show_appliance(appliances)
    
    # while = estrutura de repetição
    # True = loop infinito até encontrar break ou return
    while True:
        # loop interno para validar ID do aparelho
        while True:
            # solicita ID do aparelho
            appliance_id = input(
                "\nDigite o ID do aparelho"
                "(ou 0 para finalizar): "
            )
            # verifica se usuário quer finalizar cadastro
            if appliance_id == "0":
                # exibe sucesso
                show_success("Cadastro concluído.")
                # finaliza função
                return
            # Verifica se ID é válido
            if validate_id(appliance_id):
                # break = encerra loop atual
                break
            # Caso ID seja inválido aparece essa mensagem
            show_error("ID inválido.")
        # Loop para validar tempo diário
        while True:
            # solicita minutos de uso diário ao usuário
            daily_usage = input(
             "Tempo médio diário de uso (minutos): "
            )
            # verifica se o valor é positivo
            if validate_positive_number(daily_usage):
                # sai do loop
                break
            # Monstra mensagem se houve erro
            show_error("Digite um número válido.")
        # Loop para validar quantidade de dias de uso por mês
        while True:
            # Recebe o valor de dias por mês do usuário
            monthly_days = input(
                "Quantos dias por mês utiliza: "
            )
            # verifica se o valor inserido é valido
            if validate_positive_number(monthly_days):
                # sai do loop
                break
            # mostra erro se houver
            show_error("Digite um número válido.")
        # chama service para salvar aparelho do usuário
        create_user_appliance_service(
            # ID do usuário criado
            user["id"],
            # ID do aparelho
            appliance_id,
            # Tempo de uso diário em minutos
            daily_usage,
            # Dias de uso por mês
            monthly_days
        )

# Função responsável pelo login
def login_user_controller():
    # solicita e-mail
    email = input("\nDigite seu e-mail: ")
    # chama service de login
    user, error = login_user_service(email)
    # verifica erro
    if error:
        # mostra erro
        show_error(error)
        # encerra função
        return
    # exibe mensagem de boas-vindas
    show_success(
        f"Bem-vindo, {user['name']}!"
    )
    # abre menu do usuário
    user_menu_controller(user)

# função do menu interno do usuário
def user_menu_controller(user):
    # loop infinito do menu
     while True:
        # print() = exibe texto no terminal
        # \n = quebra de linha
        print("\n===== MENU DO USUÁRIO =====")
        print("1 - Atualizar cadastro")
        print("2 - Relatórios")
        print("3 - Gerenciar aparelhos")
        print("4 - Excluir conta")
        print("0 - Logout")

        # captura opção digitada
        option = input("\nEscolha uma opção: ")
        # verifica se opção existe
        if not validate_menu_option(
            option,
            ["1", "2", "3", "4", "0"]
        ):
            # mostra erro
            print("\nOpção inválida.")
            # continue = reinicia loop atual
            continue
        
        # estrutura condicional do menu
        if option == "1":
            print("Função em desenvolvimento.")
            
        elif option == "2":
            print("Função em desenvolvimento.")
            
        elif option == "3":
            print("Função em desenvolvimento.")

        elif option == "4":
            print("Função em desenvolvimento.")

        elif option == "0":
            print("\nLogout realizado.")
            # sai do loop
            break
