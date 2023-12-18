"""
Question

Create a function 'find_closest_city'
that takes a path to data file and coordinates
and returns a name of the city closest to the provided coordinates.

Use data from file pointed by cities_data_path variable
Result should be a string.
"""
from typing import Tuple
import json

from questions import CITIES_FILE_PATH
from questions.helpers.distance import calculate_distance


# Your solution here
def find_closest_city(path: str, coordinates: Tuple[float, float]) -> str:
    with open(path) as f:
        cities = json.load(f)

    closest_city = None
    shortest_distance = float("inf")
    for city in cities:
        distance = calculate_distance(
            lat1=coordinates[0], lng1=coordinates[1], lat2=float(city.get("lat")), lng2=float(city.get("lng"))
        )
        if distance < shortest_distance:
            closest_city = city.get("city")
            shortest_distance = distance
    return closest_city


if __name__ == "__main__":
    test_coordinates = (50.103611, 19.315556)
    result = find_closest_city(path=CITIES_FILE_PATH, coordinates=test_coordinates)
    print(result)
