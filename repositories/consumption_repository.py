from utils.txt_handler import read_txt_file

def get_all_consumption_levels():
    
    levels = []

    data_list = read_txt_file(
        "./data/consumption_levels.txt",
        5
    )

    for line_number, data in enumerate(data_list, start=1):

        try:

            level = {
                "id": data[0],
                "level": data[1],
                "house_profile": data[2],
                "range": data[3],
                "profile": data[4]
            }

            levels.append(level)

        except Exception:

            print(
                f"[AVISO] Linha {line_number} "
                f"ignorada em consumption_levels.txt"
            )
    
    return levels