import csv
fraudulent_transactions_sender_ids = []

with open("foobar_2025_Question_1/user_materials/Transactions.csv", "r") as file:
    reader = csv.reader(file)
    next(reader) # bc the headings AHHHHH

    for row in reader:
        # print(row)
        sent_amount = float(row[5])
        recieved_amount = float(row[6])
        fee = float(row[8])
        # print(sent_amount, recieved_amount, fee)
        if round(sent_amount - fee, 2) != round(recieved_amount, 2):
            fraudulent_transactions_sender_ids.append(row[2])
            print(sent_amount, recieved_amount, fee, sent_amount - fee)
    

print((fraudulent_transactions_sender_ids))  