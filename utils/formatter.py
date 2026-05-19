# utils/formatter.py
# Arquivo responsável por padronizar mensagens e exibições do sistema EcoLar

def show_title(title: str):
    """
    Exibe títulos destacados de forma elegante e centralizada no terminal.
    """
    # Cria uma linha horizontal de 50 caracteres para servir de borda superior
    border = "=" * 50
    print(f"\n{border}")
    
    # O método .center(50) centraliza o texto no meio da linha de 50 espaços
    print(f"{title.upper().center(50)}")
    
    # Cria a linha horizontal de borda inferior
    print(f"{border}\n")


def show_success(message: str):
    """
    Exibe mensagens de sucesso com um indicador visual verde.
    """
    # print = exibe a mensagem de sucesso com o emoji indicador
    print(f"✅ [SUCESSO] {message}")


def show_error(message: str):
    """
    Exibe mensagens de erro com um indicador visual vermelho para dar destaque.
    """
    # print = exibe o erro para alertar o usuário sobre falhas
    print(f"❌ [ERRO] {message}")


def show_warning(message: str):
    """
    Exibe mensagens de atenção ou aviso para o usuário.
    """
    # print = exibe o aviso indicando que o usuário deve ter atenção
    print(f"⚠️ [AVISO] {message}")


def show_info(message: str):
    """
    Exibe mensagens informativas simples durante a navegação.
    """
    # print = exibe uma informação neutra do sistema
    print(f"ℹ️ [INFO] {message}")


def format_table_row(left_text: str, right_text: str, width: int = 50) -> str:
    """
    Alinha textos em formato de linha de tabela/relatório de forma automática.
    Exemplo: Geladeira .............................. 150 kWh
    """
    # Calcula quantos pontos (...) são necessários para preencher o espaço do meio
    dots_count = width - len(left_text) - len(right_text)
    
    # se o cálculo for positivo, monta a linha com os pontos alinhados
    if dots_count > 0:
        return f"{left_text} {'.' * dots_count} {right_text}"
    
    # except = caso o texto seja grande demais para os pontos, separa por uma barra
    return f"{left_text} | {right_text}"


def show_menu_options(options: list):
    """
    Exibe uma lista de opções para menus de forma automatizada e limpa.
    """
    # for = percorre a lista de opções gerando a numeração automática começando do 1
    for index, option in enumerate(options, start=1):
        print(f"  [{index}] {option}")
        
    # Exibe a opção padrão de saída do sistema
    print(f"  [0] Sair")
    
    # Cria uma linha divisória fina no final do menu
    print("-" * 50)