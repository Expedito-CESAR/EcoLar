from utils.txt_handler import read_txt_file

def get_all_tips():

    tips = []

    data_list = read_txt_file(
        "./data/tips.txt",
        3
    )

    for line_number, data in enumerate(data_list, star=1):

        try:

            tip = {
                "id": data[0],
                "appliance": data[1],
                "tip": data[2]
            }

            tips.append(tip)

        except Exception:

            print(
                f"[AVISO] Linha{line_number} "
                f"ignorada em tips.txt"
            )

    return tips