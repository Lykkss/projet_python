import csv
import os

def file_reader(file_path):
    '''
    Reads a CSV file and returns its content as a list of rows.

    Args:
        file_path (str): The relative path to the CSV file.

    Returns:
        data: A list of rows, where each row is a type of values.
        str: An error message if the file is empty.
        ValueError: If the file does not exist or is not a CSV file.
    '''
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
