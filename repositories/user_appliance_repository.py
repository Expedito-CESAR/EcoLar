# def = usado para criar funções
# create_user_appliance_repository = função responsável por salvar
# aparelhos associados ao usuário

def create_user_appliance_repository(user_appliance):


    # try = tenta executar bloco
    # usado para evitar quebra do sistema em caso de erro
    try:


        # with open() = abre arquivo TXT

        # with = gerencia abertura/fechamento automático do arquivo
        # open() = função que abre arquivos

        # "./data/user_appliances.txt" = caminho do arquivo

        # "a" = modo append
        # adiciona conteúdo sem apagar o existente

        # encoding="utf-8" = permite caracteres especiais
        with open(
            "./data/user_appliances.txt",
            "a",
            encoding="utf-8"
        ) as file:


            # write() = escreve conteúdo no arquivo TXT
            file.write(

                # f"" = f-string
                # permite inserir variáveis dentro do texto

                # user_appliance['user_id']
                # ID do usuário

                f"{user_appliance['user_id']};"

                # ID do aparelho
                f"{user_appliance['appliance_id']};"

                # Tempo médio diário de uso
                f"{user_appliance['daily_usage']};"

                # Quantidade de dias no mês

                # \n = quebra de linha
                # faz próximo registro ir para linha seguinte
                f"{user_appliance['monthly_days']}\n"
            )


    # except = executa caso aconteça erro
    # Exception = captura qualquer tipo de erro
    except Exception as error:


        # print() = exibe mensagem no terminal
        print(

            # f"" = texto com variável
            f"[ERRO] Falha ao salvar aparelho: "

            # Mostra detalhe do erro ocorrido
            f"{error}"
        )