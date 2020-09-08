"""
Question

Create a function 'check_if_higher'
that checks if one city is elevated higher than the other.

Use data from file pointed by cities_data_path variable

To get the elevation data use "https://elevation-api.io/"
with key taken from environmental variable "ELEVATION_API_KEY"

Result should be a bool:
True if city1 is higher than city2.

"""

# Your solution here
import json
from typing import Tuple

import requests
import os


def check_if_higher(path: str, city1: Tuple[float, float], city2: Tuple[float, float]) -> bool:

    base_url = r" https://elevation-api.io/api/elevation"
    params = {"points": f"({city1[0]},{city1[1]}),({city2[0]},{city2[1]})",
              "key": os.getenv("ELEVATION_API_KEY")}
    response = requests.get(url=base_url, params=params, timeout=20)

    if response:
        rj = json.loads(response.text)
        city1_elevation = float(rj["elevations"][0]["elevation"])
        city2_elevation = float(rj["elevations"][1]["elevation"])
        is_city1_higher = city1_elevation > city2_elevation
        return is_city1_higher


if __name__ == '__main__':
    from dotenv import load_dotenv

    load_dotenv()
    cities_data_path = r"data\cities.json"
    # Is Krakow elevated higher than Katowice?
    kat_coordinates = 50.258415, 19.027545
    kra_coordinates = 50.057531, 19.980216
    is_kra_higher = check_if_higher(path=cities_data_path, city1=kra_coordinates, city2=kat_coordinates)
    print(is_kra_higher)
