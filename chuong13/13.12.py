from csv import reader
with open('data_1.csv','r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        print(row)