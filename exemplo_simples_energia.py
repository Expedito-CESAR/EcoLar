# exemplo_simples_energia.py
# Exemplo muito simples - pode copiar e colar
# So usa if/print/for

from controllers.energy_simple_controller import (
    mostrar_consumo_simples,
    mostrar_classificacao,
    mostrar_economia_simples,
    mostrar_opcoes_economia
)

print("\n" + "="*70)
print("EXEMPLO SIMPLES - SISTEMA DE CONSUMO DE ENERGIA")
print("="*70)

# Cria usuario fake para testar
usuario_teste = {
    "id": "001",
    "name": "Expedito"
}

# MOSTRA OPCAO 1
print("\n>>> OPCAO 1: Consumo simples")
mostrar_consumo_simples(usuario_teste)

# MOSTRA OPCAO 2
print("\n>>> OPCAO 2: Classificacao")
mostrar_classificacao(usuario_teste)

# MOSTRA OPCAO 3
print("\n>>> OPCAO 3: Economia simples")
mostrar_economia_simples(usuario_teste)

# MOSTRA OPCAO 4
print("\n>>> OPCAO 4: Opcoes de economia")
mostrar_opcoes_economia(usuario_teste)

print("\n" + "="*70)
print("FIM DO EXEMPLO")
print("="*70 + "\n")
