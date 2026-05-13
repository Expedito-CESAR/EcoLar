from utils.txt_handler import read_txt_file

def get_all_history():

    history = []

    data_list = read_txt_file(
        "./data/history.txt",
        5
    )

    for line_number, data in enumerate(data_list, start=1):

        try:

            history_item = {
                "data": data[0],
                "user": data[1],
                "appliance": data[2],
                "consumption": float(data[3]),
                "cost": float(data[4])
            }

            history.append(history_item)
        
        except ValueError:
            print(
                f"[AVISO] Linha {line_number} "
                f"ignorada em history.txt"
            )
    
    return history