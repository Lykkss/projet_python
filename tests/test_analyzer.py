import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from analyzer import analyze_csv

def test_analyze_csv():
    file_path = "day_wise.csv"
    data_dir = 'data'
    full_file_path = os.path.join(data_dir, file_path)

    if not os.path.exists(full_file_path):
        print(f"Error: {full_file_path} does not exist. Please check the file path.")
        return
    
    print(f"Running analysis on {file_path}...\n")
    summary = analyze_csv(file_path)
    print(summary)

if __name__ == "__main__":
    test_analyze_csv()
