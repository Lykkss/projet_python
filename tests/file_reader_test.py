import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from file_reader import file_reader

if __name__ == '__main__':
    print(file_reader('day_wise.csv'))
