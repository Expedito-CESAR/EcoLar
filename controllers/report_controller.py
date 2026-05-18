# report_controller.py
# Controller responsável pelos relatórios do sistema

# Importa repositories
from repositories.user_appliance_repository import (
    get_user_appliances_by_user_id
)

from repositories.appliance_repository import (
    get_all_appliances
)

from repositories.tip_repository import (
    get_all_tips
)

# Exibe relatório simples de consumo
def show_consumption_report_controller(user):

    print("\n===== RELATÓRIO ENERGÉTICO =====")

    # Busca aparelhos do usuário
    user_appliances = (
        get_user_appliances_by_user_id(user["id"])
    )

    # Busca aparelhos cadastrados
    appliances = get_all_appliances()

    # Variável acumuladora
    total_consumption = 0

    # Percorre aparelhos do usuário
    for user_appliance in user_appliances:

        # Procura aparelho correspondente
        for appliance in appliances:

            # Verifica correspondência
            if (
                appliance["id"]
                ==
                user_appliance["appliance_id"]
            ):

                print(
                    f"\n{appliance['name']}"
                )

                print(
                    f"Consumo base: "
                    f"{appliance['consumption']} kWh"
                )

                # Soma consumo
                total_consumption += (
                    appliance["consumption"]
                )

    # Exibe total
    print(
        f"\nConsumo total estimado: "
        f"{total_consumption} kWh"
    )

# Exibe recomendações energéticas
def show_recommendations_controller(user):

    print("\n===== RECOMENDAÇÕES =====")

    # Busca aparelhos do usuário
    user_appliances = (
        get_user_appliances_by_user_id(user["id"])
    )

    # Busca aparelhos
    appliances = get_all_appliances()

    # Busca dicas
    tips = get_all_tips()

    # Percorre vínculos
    for user_appliance in user_appliances:

        # Procura aparelho correspondente
        for appliance in appliances:

            if (
                appliance["id"]
                ==
                user_appliance["appliance_id"]
            ):

                print(
                    f"\n{appliance['name']}"
                )

                # Busca dicas do aparelho
                for tip in tips:

                    if (
                        tip["appliance"]
                        ==
                        appliance["name"]
                    ):

                        print(
                            f"- {tip['tip']}"
                        )


# Simulação simples de economia
def show_simulation_controller(user):

    print("\n===== SIMULAÇÃO DE ECONOMIA =====")

    print(
        "\nReduzindo 30 minutos diários "
        "de uso em aparelhos de alto consumo."
    )

    print(
        "\nEconomia estimada: "
        "5% a 15% ao mês."
    )