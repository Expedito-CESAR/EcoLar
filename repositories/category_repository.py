from utils.txt_handler import read_txt_file

def get_all_categories():

    categories = []

    data_list = read_txt_file(
        "./data/categories.txt",
        3
    )

    for line_number, data in enumerate(data_list, start=1):

        try:

            category = {
                "id": data[0],
                "name": data[1],
                "description": data[2]
            }

            categories.append(category)

        except Exception:

            print(
                f"[AVISO] Linha {line_number} "
                f"ignorada em categories.txt"
            )

    return categories