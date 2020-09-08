"""
Question

Create a function 'check_if_higher'
that checks if one city is elevated higher than the other.

Use data from file pointed by cities_data_path variable

To get the elevation data use "https://elevation-api.io/"
with API Key provided by an interviewer

Result should be a bool:
True if city1 is higher than city2.

"""

# Your solution here
import json
from typing import Tuple

import requests


def check_if_higher(path: str, city1: Tuple[float, float], city2: Tuple[float, float]) -> bool:
    pass


if __name__ == '__main__':
    cities_data_path = r"data\cities.json"
    # Is Krakow elevated higher than Katowice?
    kat_coordinates = 50.258415, 19.027545
    kra_coordinates = 50.057531, 19.980216
    is_kra_higher = check_if_higher(path=cities_data_path, city1=kra_coordinates, city2=kat_coordinates)
    print(is_kra_higher)
