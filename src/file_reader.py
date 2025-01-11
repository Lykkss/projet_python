import csv

def file_reader(file_path):
    file_path = 'data/' + file_path
    data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data
