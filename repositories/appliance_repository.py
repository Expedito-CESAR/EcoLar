# from = usado para importar partes específicas de outro arquivo
# import = traz funções/classes/módulos para este arquivo

# Importa função responsável por ler arquivos TXT
# utils = pasta de utilidades auxiliares do sistema
from utils.txt_handler import read_txt_file

# def = usado para criar funções
# get_all_appliances = função responsável por buscar todos os aparelhos
def get_all_appliances():
    # Lista vazia onde os aparelhos serão armazenados
    appliances = []
    # Chama função que lê o arquivo TXT
    # "./data/appliances.txt" = caminho do arquivo
    # 8 = quantidade esperada de colunas por linha
    data_list = read_txt_file(
        "./data/appliances.txt",
        8
    )

    # for = estrutura de repetição
    # percorre todos os itens da lista

    # enumerate() = adiciona contador durante repetição
    # line_number = número da linha
    # data = conteúdo da linha
    # start=1 = contador começa em 1
    for line_number, data in enumerate(data_list, start=1):

        # try = tenta executar bloco
        # usado para evitar quebra do sistema
        try:
            # Cria dicionário representando aparelho
            # dict = estrutura chave:valor
            appliance = {
                # data[0] = primeira coluna do TXT
                "id": data[0],   
                # Categoria do aparelho      
                "category": data[1],  
                # Nome do aparelho    
                "name": data[2],  
                # float() = converte valor para número decimal
                # Potência elétrica do aparelho      
                "power": float(data[3]),
                # int() = converte valor para número inteiro
                # Tempo médio de uso
                "usage_time": int(data[4]),
                # Quantidade de dias de uso
                "days": int(data[5]),
                # Consumo energético
                "consumption": float(data[6]),
                # Nível de consumo
                "level": data[7]
            }
            # append() = adiciona item na lista
            appliances.append(appliance)

        # except = executa caso erro aconteça
        # ValueError = erro de conversão numérica
        except ValueError:

            # f"" = f-string
            # permite inserir variáveis dentro do texto
            print(
                # Exibe aviso no terminal
                f"[AVISO] Linha {line_number} "
                # Mensagem complementar
                f"ignorada em appliances.txt"
            )
        
    # return = devolve valor da função
    # retorna lista completa de aparelhos
    return appliances