# from = usado para importar partes específicas de outro arquivo
# import = traz funções/classes/módulos para este arquivo
# Importa função principal do sistema
# controllers = camada responsável por controlar o fluxo do sistema
from controllers.menu_controller import start_system

# print() = exibe texto no terminal
# \n = quebra de linha
print("Sistema EcoLar iniciado\n")

# Chama função responsável por iniciar sistema
# start_system() = ponto inicial da navegação
start_system()