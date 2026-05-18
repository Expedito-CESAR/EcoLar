# appliance_controller.py
# Controller responsável pelos aparelhos do sistema

# Importa repositories
from repositories.appliance_repository import (
    get_all_appliances
)

from repositories.user_appliance_repository import (
    get_user_appliances_by_user_id
)

# Importa views
from views.appliance_view import (
    show_appliance
)

# Exibe aparelhos cadastrados pelo usuário
def list_user_appliances_controller(user):

    print("\n===== MEUS APARELHOS =====")

    # Busca vínculos do usuário
    user_appliances = (
        get_user_appliances_by_user_id(user["id"])
    )

    # Busca aparelhos disponíveis
    appliances = get_all_appliances()

    # Percorre vínculos
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
                    f"Uso diário: "
                    f"{user_appliance['daily_usage']} min"
                )

                print(
                    f"Dias no mês: "
                    f"{user_appliance['monthly_days']}"
                )
