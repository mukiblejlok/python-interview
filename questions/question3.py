"""
Question

Create a function 'check_if_higher'
that checks if one city is elevated higher than the other.

Use data from file pointed by cities_data_path variable

To get the elevation data use `https://api.open-elevation.com/api/v1/lookup`
Check the docs for API: https://github.com/Jorl17/open-elevation/blob/master/docs/api.md

Result should be a bool:
True if city1 is higher than city2.

"""

# Your solution here
import json
from typing import Tuple

import requests


def check_if_higher(city1: Tuple[float, float], city2: Tuple[float, float]) -> bool:
    pass


if __name__ == "__main__":
    # Is Krakow elevated higher than Katowice?
    katowice_coordinates = 50.258415, 19.027545  # Expected elevation 264
    krakow_coordinates = 50.057531, 19.980216  # Expected elevation 204
    is_kra_higher = check_if_higher(city1=krakow_coordinates, city2=katowice_coordinates)
    print(is_kra_higher)
