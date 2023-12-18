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
    with open(path, "r") as f:
        cities = json.load(f)

    cities_with_pop = [c for c in cities if c.get("population")]
    sorted_cities = sorted(cities_with_pop, key=lambda c: float(c.get("population", 0)), reverse=True)
    top_10_cities = [city.get("city") for city in sorted_cities][:10]
    return top_10_cities


if __name__ == "__main__":
    top_10 = find_top_10(path=CITIES_FILE_PATH)
    print(top_10)
