# formatter.py
# Arquivo responsável por padronizar mensagens do sistema

# Exibe títulos fomatados
def show_title(title):
    
    print(f"\n===== {title.upper()} =====")

# Exibe mensagens de sucesso
def show_success(message):
    
    print(f"\n[SUCESSO] {message}")

# Exibe mensagem de erro
def show_error(message):

    print(f"\n[ERRO] {message}")

# Exibe mensagens de aviso
def show_warning(message):

    print(f"\n[AVISO] {message}")

# Exibe mensagens informativas
def show_info(message):

    print(f"\n[INFO] {message}")