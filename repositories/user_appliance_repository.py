def create_user_appliance_repository(user_appliance):
    
    try:

        with open(
            "./data/user_appliances.txt",
            "a",
            encoding="utf-8"
        ) as file:
            
            file.write(
                f"{user_appliance['user_id']};"
                f"{user_appliance['appliance_id']};"
                f"{user_appliance['daily_usage']};"
                f"{user_appliance['monthly_days']}\n"
            )

    except Exception as error:
        print(
            f"[ERRO] Falha ao salvar aparelho: "
            f"{error}"
        )