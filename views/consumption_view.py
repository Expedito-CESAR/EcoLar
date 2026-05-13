def show_consumption_levels(levels):

    print("\n===== PERFIS DISPONÍVEIS =====\n")

    for level in levels:
        print(
            f"{level['id']} - "
            f"{level['level']} "
            f"({level['profile']})"
        )