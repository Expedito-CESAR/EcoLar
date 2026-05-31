# energy_controller.py

from services.consumption_service import (
    calculate_user_consumption,
    calculate_cost
)

from services.energy_classification_service import (
    classify_consumption,
    compare_with_average,
    classify_by_range
)

from services.simulation_service import (
    simulate_savings,
    simulate_multiple_reductions
)

from views.user_view import (
    show_error
)

from utils.formatter import (
    show_title
)


def show_consumption(user):

    show_title("Consumo de Energia")

    consumption = calculate_user_consumption(user["id"])

    cost = calculate_cost(consumption)

    print(f"Consumo mensal: {consumption} kWh")
    print(f"Custo mensal: R$ {cost}")


def show_classification(user):

    show_title("Classificação Energética")

    data = classify_consumption(user["id"])

    print(f"Consumo: {data['consumption_kwh']} kWh")
    print(f"Classificacao: {data['classification']}")

    comparison = compare_with_average(user["id"])

    print(f"\nComparacao com media nacional:")
    print(f"Media nacional: {comparison['national_average_kwh']} kWh")
    print(f"Seu consumo: {comparison['status']} da media")

    range_class = classify_by_range(user["id"])
    print(f"\nFaixa: {range_class}")


def show_savings(user):

    show_title("Economia Potencial")

    savings = simulate_savings(user["id"], 30)

    print(f"Consumo atual: {savings['current_consumption_kwh']} kWh")
    print(f"Custo atual: R$ {savings['current_cost_reais']}")

    print(f"\nSe reduzir {savings['reduction_percentage']}%:")
    print(f"Novo consumo: {savings['new_consumption_kwh']} kWh")
    print(f"Novo custo: R$ {savings['new_cost_reais']}")

    print(f"\nEconomia:")
    print(f"Por mes: R$ {savings['monthly_savings_reais']}")
    print(f"Por ano: R$ {savings['annual_savings_reais']}")


def show_savings_options(user):

    print("\n===== OPCOES DE ECONOMIA =====\n")

    data = simulate_multiple_reductions(user["id"])

    print(f"Consumo atual: {data['current_consumption']} kWh (R$ {data['current_cost']})")
    print("\n--- OPCAO 1: Reduzir 10% ---")
    opt1 = data["option_10_percent"]
    print(f"Novo consumo: {opt1['new_consumption']} kWh")
    print(f"Economia mensal: R$ {opt1['monthly_savings']}")
    print(f"Economia anual: R$ {opt1['annual_savings']}")

    print("\n--- OPCAO 2: Reduzir 20% ---")
    opt2 = data["option_20_percent"]
    print(f"Novo consumo: {opt2['new_consumption']} kWh")
    print(f"Economia mensal: R$ {opt2['monthly_savings']}")
    print(f"Economia anual: R$ {opt2['annual_savings']}")

    print("\n--- OPCAO 3: Reduzir 30% ---")
    opt3 = data["option_30_percent"]
    print(f"Novo consumo: {opt3['new_consumption']} kWh")
    print(f"Economia mensal: R$ {opt3['monthly_savings']}")
    print(f"Economia anual: R$ {opt3['annual_savings']}")

# Controller responsável pelo submenu energético
# Centraliza funcionalidades relacionadas ao consumo

def show_energy_menu_controller(user):

    # Loop do submenu energético
    while True:

        show_title("Energia")

        print("1 - Ver consumo")
        print("2 - Ver classificação")
        print("3 - Simular economia")
        print("4 - Opções de economia")
        print("0 - Voltar")

        # Captura opção do usuário
        option = input(
            "\nEscolha uma opção: "
        )

        # Exibe consumo energético
        if option == "1":

            show_consumption(user)

        # Exibe classificação energética
        elif option == "2":

            show_classification(user)

        # Exibe simulação simples
        elif option == "3":

            show_savings(user)

        # Exibe múltiplas opções de economia
        elif option == "4":

            show_savings_options(user)

        # Retorna ao menu anterior
        elif option == "0":

            break

        # Trata opções inválidas
        else:

            show_error("Opção inválida.")