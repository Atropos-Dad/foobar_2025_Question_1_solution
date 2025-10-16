import numpy as np
import pandas as df


with open("user_materials/Users.csv") as f:
    # df from csv
    users = df.read_csv(f)

    transactions = df.read_csv("user_materials/Transactions.csv")

    blacklist = df.read_csv("user_materials/Blacklist.csv")

# for transaction in transactions - first check if entity_id in blacklist.csv
def find_blacklisted():
    blacklisted_entities = []    
    sus_transactions = []

    for index, row in blacklist.iterrows():
        blacklisted_entities.append({"ID": row["ENTITY_ID"], "DATE": row["DATE_ADDED"]})

    for index, row in transactions.iterrows():
        sender_id = row["SENDER_ID"]
        recipient_id = row["RECIPIENT_ID"]

        # Check if BOTH sender and recipient are in blacklist
        blacklist_dict_row_sender = next((i for i in blacklisted_entities if i["ID"] == sender_id), None)
        blacklist_dict_row_recipient = next((i for i in blacklisted_entities if i["ID"] == recipient_id), None)

        if blacklist_dict_row_sender and blacklist_dict_row_recipient:
            print("found both sender and reciever")
            transaction_row_date = row["DATE_TIME"].split(" ")[0]

            # Compare transaction date with both blacklist dates
            import datetime
            format = "%d/%m/%Y"
            datetime_transaction = datetime.datetime.strptime(transaction_row_date, format)
            datetime_blacklist_sender = datetime.datetime.strptime(blacklist_dict_row_sender["DATE"], format)
            datetime_blacklist_recipient = datetime.datetime.strptime(blacklist_dict_row_recipient["DATE"], format)

            # Only add if transaction is after BOTH blacklist dates
            if (datetime_transaction >= datetime_blacklist_sender):
                # datetime_transaction >= datetime_blacklist_recipient):
                print("found valid one!")
                sus_transactions.append(row)
            
    print(sus_transactions)

find_blacklisted()