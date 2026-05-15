# views = camada responsável pela interface visual/textual do sistema
# separação de interface =
# toda comunicação com usuário fica isolada nesta camada
# Isso facilita:
# - organização do código
# - manutenção
# - futuras melhorias
# Exemplo:
# Hoje usamos terminal
# Amanhã poderia virar:
# - interface web
# - aplicativo
# - interface gráfica

# Sem precisar alterar services/repositories

# def = usado para criar funções
# show_user_registration_title = função responsável
# por exibir título do cadastro

def show_user_registration_title():

    # print() = exibe texto no terminal
    # \n = quebra de linha
    print("\n===== CADASTRO DE USUÁRIO =====\n")

# Função responsável por solicitar nome do usuário
def get_user_name():

    # return = devolve valor da função
    # input() = captura texto digitado no terminal
    return input("Digite seu nome: ")

# Função responsável por solicitar e-mail
def get_user_email():

    # Captura e devolve e-mail digitado
    return input("Digite seu e-mail: ")

# Função responsável por solicitar data de aniversário
def get_user_birthday():

    # Captura e devolve data digitada
    return input("Digite sua data de aniversário: ")

# Função responsável por exibir mensagens de erro
def show_error(message):

    # f"" = f-string
    # permite inserir variáveis dentro do texto
    # message = mensagem recebida como parâmetro
    print(f"\n[ERRO] {message}")

# Função responsável por exibir mensagens de sucesso
def show_success(message):

    # Exibe mensagem formatada de sucesso
    print(f"\n[SUCESSO] {message}")