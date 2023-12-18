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
import os
from typing import Tuple

import requests


def check_if_higher(city1: Tuple[float, float], city2: Tuple[float, float]) -> bool:
    base_url = r"https://api.open-elevation.com/api/v1/lookup"
    params = {"locations": f"{city1[0]},{city1[1]}|{city2[0]},{city2[1]}"}
    response = requests.get(url=base_url, params=params, timeout=20)

    if response:
        rj = json.loads(response.text)
        city1_elevation = float(rj["results"][0]["elevation"])
        city2_elevation = float(rj["results"][1]["elevation"])
        is_city1_higher = city1_elevation > city2_elevation
        print("City1 Elevation: ", city1_elevation)
        print("City2 Elevation: ", city2_elevation)
        return is_city1_higher


if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()
    # Is Krakow elevated higher than Katowice?
    katowice_coordinates = 50.258415, 19.027545  # Expected elevation 264
    krakow_coordinates = 50.057531, 19.980216    # Expected elevation 204
    is_kra_higher = check_if_higher(city1=krakow_coordinates, city2=katowice_coordinates)
    print(is_kra_higher)
