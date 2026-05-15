# def = usado para criar funções

# show_appliance = função responsável por exibir
# aparelhos disponíveis no terminal

def show_appliance(appliances):

    # print() = exibe texto no terminal

    # \n = quebra de linha
    print("\n===== APARELHOS DISPONÍVEIS =====\n")

    # for = estrutura de repetição
    # percorre todos os aparelhos da lista

    # appliance = representa cada aparelho individualmente
    for appliance in appliances:

        # Exibe informações do aparelho
        print(

            # f"" = f-string
            # permite inserir variáveis dentro do texto

            # appliance['id']
            # acessa ID do aparelho no dicionário
            f"{appliance['id']} - "

            # appliance['name']
            # acessa nome do aparelho
            f"{appliance['name']}"
        )