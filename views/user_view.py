# separação de interface; facilitação de futuras telas; facilitação de interface web futura.
# Não faremos interface no projeto, mas já deixaremos pronto o que for possível para melhorias

def show_user_registration_title():
    print("\n===== CADASTRO DE USUÁRIO =====\n")

def get_user_name():
    return input("Digite seu nome: ")

def get_user_email():
    return input("Digite seu e-mail: ")

def get_user_birthday():
    return input("Digite sua data de aniversário: ")

def show_error(message):
    print(f"\n[ERRO] {message}")

def show_success(message):
    print(f"\n[SUCESSO] {message}")