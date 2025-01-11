import csv
import os

def file_reader(file_path):
    file_path = 'data/' + file_path
    if not os.path.exists(file_path):
        return ValueError('File does not exist.')
    elif not file_path.endswith('.csv'):
        return ValueError('Invalid file format. Only CSV files are supported.')
    data = []
    with open(file_path, 'r') as file:
        content = file.read()
        if len(content) == 0:
            return "File is empty"
        csv_reader = csv.reader(content.splitlines())
        for row in csv_reader:
            data.append(row)
    return data
