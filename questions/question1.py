"""
Question

Find top ten biggest cities.

Create a function 'find_top_10' that takes a path to a data file
and returns a list of top 10 biggest cities.
Use data from file pointed by cities_data_path variable
Result should be in form of a list of strings.
"""
from typing import List
import json

from questions import CITIES_FILE_PATH


# Your solution here
def find_top_10(path: str) -> List[str]:
    pass


if __name__ == "__main__":
    top_10 = find_top_10(path=CITIES_FILE_PATH)
    print(top_10)
