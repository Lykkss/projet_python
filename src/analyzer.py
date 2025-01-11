import pandas as pd
from file_reader import file_reader

def analyze_csv(file_path):
    # Read data using file_reader
    raw_data = file_reader(file_path)

    # Convert raw data (list of lists) to DataFrame
    if isinstance(raw_data, list):
        try:
            # Assume the first row contains headers
            df = pd.DataFrame(raw_data[1:], columns=raw_data[0])
        except IndexError:
            print("Error: The CSV file seems to be empty or malformed.")
            return None
    else:
        print("Error: Unsupported data format.")
        return None

    # Convert numeric columns to proper datatypes
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col], errors='ignore')
        except ValueError:
            pass

    # Generate summary statistics
    print("Statistical Summary:")
    print(df.describe(include='all'))

# Example usage
if __name__ == "__main__":
    file_name = "your_file.csv"  # Replace with your CSV file name
    analyze_csv(file_name)
