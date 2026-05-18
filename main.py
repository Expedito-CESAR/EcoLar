# main.py
# Arquivo principal do sistema EcoLar

# Importa função responsável
# por iniciar o sistema
from controllers.menu_controller import (
    start_system
)

# Exibe mensagem inicial
print("\nSistema EcoLar iniciado.")

# Inicializa sistema
start_system()