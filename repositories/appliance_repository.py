from utils.txt_handler import read_txt_file

def get_all_appliances():
    appliances = []
    data_list = read_txt_file(
        "./data/appliances.txt",
        8
    )

    for line_number, data in enumerate(data_list, start=1):

        try:
            appliance = {
                "id": data[0],
                "category": data[1],
                "name": data[2],
                "power": float(data[3]),
                "usage_time": int(data[4]),
                "days": int(data[5]),
                "consumption": float(data[6]),
                "level": data[7]
            }

            appliances.append(appliance)

        except ValueError:

            print(
                f"[AVISO] Linha {line_number} "
                f"ignorada em appliances.txt"
            )
        

    return appliances