import csv

fraudulent_transactions_sender_ids = []

with open("foobar_2025_Question_1/user_materials/Transactions.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # GWAY header 
    for row in reader:
        sender_id = (row[2])

        with open("foobar_2025_Question_1/user_materials/Users.csv", "r") as user_file:
            user_reader = csv.reader(user_file)
            next(user_reader)  #  header 
            for user_row in user_reader:
                if user_row[0] == sender_id:
                    device_id = user_row[4]
                    country = user_row[5]

                    with open("foobar_2025_Question_1/user_materials/Devices.csv", "r") as device_file:
                        device_reader = csv.reader(device_file)
                        next(device_reader)  # HEADER
                        for device_row in device_reader:
                            if device_row[0] == device_id:
                                device_country = device_row[3]
                                if device_country != country:
                                    fraudulent_transactions_sender_ids.append(sender_id)
