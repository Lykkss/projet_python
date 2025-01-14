import pandas as pd
from .file_reader import file_reader

"""
Analyzes a CSV file and provides a statistical summary using pandas.

Args:
    file_path (str): The relative path to the CSV file to be analyzed. 
                      The file is expected to be located in the 'data' directory.

Returns:
    pandas.DataFrame: The statistical summary of the CSV data, including count, 
                       mean, std, min, max for numeric columns, and unique values 
                       for categorical columns.
"""
def analyze_csv(file_path):
    
    raw_data = file_reader(file_path)

    if isinstance(raw_data, list):
        try:
            df = pd.DataFrame(raw_data[1:], columns=raw_data[0])
        except IndexError:
            print("Error: The CSV file seems to be empty or malformed.")
            return None
    else:
        print("Error: Unsupported data format.")
        return None

    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col])
        except ValueError:
            pass

    return df.describe(include='all')