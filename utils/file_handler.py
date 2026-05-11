# utils/file_handler.py


# Função responsável pela leitura genérica de arquivos TXT
def read_txt_file(path, expected_fields):

    # Lista que armazenará os dados válidos
    data_list = []

    try:

        # Abre o arquivo em modo leitura
        with open(path, "r", encoding="utf-8") as file:

            # Percorre o arquivo linha por linha
            for line_number, line in enumerate(file, start=1):

                # Remove espaços e quebras de linha
                line = line.strip()

                # Ignora linhas vazias
                if not line:
                    continue

                # Divide os dados utilizando ";" como delimitador
                data = line.split(";")

                # Verifica se a linha possui a quantidade correta de campos
                if len(data) != expected_fields:

                    print(
                        f"[AVISO] Linha {line_number} ignorada em "
                        f"{path}: quantidade inválida de campos."
                    )

                    continue

                # Adiciona os dados válidos na lista
                data_list.append(data)

    # Trata erro caso o arquivo não exista
    except FileNotFoundError:

        print(f"[ERRO] Arquivo não encontrado: {path}")

    # Trata outros erros inesperados
    except Exception as error:

        print(f"[ERRO] Falha ao ler o arquivo {path}: {error}")

    # Retorna os dados lidos
    return data_list


# Função responsável pela leitura dos aparelhos
def read_appliances():

    print("Função executada")

    # Lista que armazenará os aparelhos
    appliances = []

    # Realiza a leitura do arquivo
    data_list = read_txt_file(
        "./data/appliances.txt",
        8
    )

    # Percorre os dados retornados
    for line_number, data in enumerate(data_list, start=1):

        try:

            # Cria um dicionário organizado para cada aparelho
            appliance = {

                "id": data[0],

                "category": data[1],

                "name": data[2],

                "power": float(data[3]),

                "usage_time": int(data[4]),

                "days": int(data[5]),

                "consumption": float(data[6]),

                "level": data[7]
            }

            # Adiciona o aparelho na lista final
            appliances.append(appliance)

        # Trata erros de conversão
        except ValueError:

            print(
                f"[AVISO] Linha {line_number} ignorada em "
                f"appliances.txt: erro de conversão."
            )

    print(appliance)

    # Retorna a lista final
    return appliances


# Função responsável pela leitura das categorias
def read_categories():

    # Lista que armazenará as categorias
    categories = []

    # Realiza a leitura do arquivo
    data_list = read_txt_file(
        "./data/categories.txt",
        3
    )

    # Percorre os dados retornados
    for line_number, data in enumerate(data_list, start=1):

        try:

            # Cria um dicionário organizado para cada categoria
            category = {

                "id": data[0],

                "name": data[1],

                "description": data[2]
            }

            # Adiciona a categoria na lista
            categories.append(category)

        # Trata erros inesperados
        except Exception:

            print(
                f"[AVISO] Linha {line_number} ignorada em "
                f"categories.txt."
            )

    # Retorna a lista final
    return categories


# Função responsável pela leitura dos níveis de consumo
def read_consumption_levels():

    # Lista que armazenará os níveis
    levels = []

    # Realiza a leitura do arquivo
    data_list = read_txt_file(
        "./data/consumption_levels.txt",
        5
    )

    # Percorre os dados retornados
    for line_number, data in enumerate(data_list, start=1):

        try:

            # Cria um dicionário organizado para cada nível
            level = {

                "id": data[0],

                "level": data[1],

                "profile": data[2],

                "consumption_range": data[3],

                "classification": data[4]
            }

            # Adiciona o nível na lista
            levels.append(level)

        # Trata erros inesperados
        except Exception:

            print(
                f"[AVISO] Linha {line_number} ignorada em "
                f"consumption_levels.txt."
            )

    # Retorna a lista final
    return levels


# Função responsável pela leitura das dicas
def read_tips():

    # Lista que armazenará as dicas
    tips = []

    # Realiza a leitura do arquivo
    data_list = read_txt_file(
        "./data/tips.txt",
        3
    )

    # Percorre os dados retornados
    for line_number, data in enumerate(data_list, start=1):

        try:

            # Cria um dicionário organizado para cada dica
            tip = {

                "id": data[0],

                "appliance": data[1],

                "tip": data[2]
            }

            # Adiciona a dica na lista
            tips.append(tip)

        # Trata erros inesperados
        except Exception:

            print(
                f"[AVISO] Linha {line_number} ignorada em "
                f"tips.txt."
            )

    # Retorna a lista final
    return tips


# Função responsável pela leitura dos usuários
def read_users():

    # Lista que armazenará os usuários
    users = []

    # Realiza a leitura do arquivo
    data_list = read_txt_file(
        "./data/users.txt",
        3
    )

    # Percorre os dados retornados
    for line_number, data in enumerate(data_list, start=1):

        try:

            # Cria um dicionário organizado para cada usuário
            user = {

                "id": data[0],

                "name": data[1],

                "email": data[2]
            }

            # Adiciona o usuário na lista
            users.append(user)

        # Trata erros inesperados
        except Exception:

            print(
                f"[AVISO] Linha {line_number} ignorada em "
                f"users.txt."
            )

    # Retorna a lista final
    return users


# Função responsável pela leitura do histórico
def read_history():

    # Lista que armazenará o histórico
    history = []

    # Realiza a leitura do arquivo
    data_list = read_txt_file(
        "./data/history.txt",
        5
    )

    # Percorre os dados retornados
    for line_number, data in enumerate(data_list, start=1):

        try:

            # Cria um dicionário organizado para cada registro
            history_item = {

                "date": data[0],

                "user": data[1],

                "appliance": data[2],

                "consumption": float(data[3]),

                "cost": float(data[4])
            }

            # Adiciona o registro na lista
            history.append(history_item)

        # Trata erros de conversão
        except ValueError:

            print(
                f"[AVISO] Linha {line_number} ignorada em "
                f"history.txt: erro de conversão."
            )

    # Retorna a lista final
    return history


# Executa testes locais do módulo
if __name__ == "__main__":

    print("\n========== APPLIANCES ==========\n")
    print(read_appliances())

    print("\n========== CATEGORIES ==========\n")
    print(read_categories())

    print("\n===== CONSUMPTION LEVELS =====\n")
    print(read_consumption_levels())

    print("\n============= TIPS =============\n")
    print(read_tips())

    print("\n============ USERS ============\n")
    print(read_users())

    print("\n=========== HISTORY ===========\n")
    print(read_history())