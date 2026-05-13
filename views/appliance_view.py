def show_appliance(appliances):

    print("\n===== APARELHOS DISPONÍVEIS =====\n")

    for appliance in appliances:
        print(
            f"{appliance['id']} - "
            f"{appliance['name']}"
        )