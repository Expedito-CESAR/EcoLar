# from = usado para importar partes especificas de outra arquivo
# import = traz funções/classes/módulos para este arquivos
# importa função responsável por ler arquivo txt
# utils = pasta de utilidades auxiliares do sistemas
from utils.txt_handler import read_txt_file

# def = usado para criar funções
# get_all_user_appliances = função responsável por buscar todos os vínculos 
# entre usuários e aparelhos
def get_all_user_appliances():
    # lista vazia onde os vínculos serão armazenados
    user_appliances = []

    # chama função responsável por ler o arquivo txt
    # "./data/user_appliances.txt" = caminho do arquivo
    # 4 = quantidade esperada de colunas por linha
    data_list = read_txt_file(
        "./data/ser_appliance.txt", 
        4
    )

    # for = estrutura de repetição
    # percorre todos os dados do arquivo
    # enumerate() = adiciona contador ao loop
    # line_number = número da linha
    # data = conteúdo da linha
    # start=1 = contador começa em 1
    for line_number, data in enumerate(data_list, start=1):

        # try = tenta executar bloco
        # usado para evitar quebra do sistema
        try:

            # verifica se IDs possuem apenas números
            # isdigit() = verifica se texto possui apenas caracteres numéricos
            if not data[0].isdigit():
                continue
            if not data[1].isdigit():
                continue

            # int() = converte valor para numero inteiro
            daily_usage = int(data[2])

            # int() = converte valor para numero inteiro
            monthly_days = int(data[3])

            # verifica se os valores são positivos
            if (
               daily_usage < 0
               or monthly_days < 0
            ):
                continue

            # cria dicionário representando vínculo
            # dict = estrutura chave:valor
            user_appliance = {
                # ID do usuário
                "user_id": data[0],
                # ID do aparelho
                "appliance_id": data[1],
                # Tempo médio diário de uso
                "daily_usage": daily_usage,
                # Quantidade de dias utilizados no mês
                "monthly_days": monthly_days,
            }
            
            # append() = adiciona item na lista
            user_appliances.append(user_appliance)

        # except = executa caso aconteça erro 
        # ValueError = erro de conversão numérica
        except ValueError:

            # print() = exibe aviso no terminal
            print (
                #mostra linha problemática
                f"[AVISO] Linha {line_number} " 
                # Complementa mensagem
                f"ignorada em user_appliances.txt"
            )

    # retorn = devolve valor da função
    # retorna lista completa de vínculos válidos 
    return user_appliances                   
     
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