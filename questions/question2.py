"""
Question

Create a function 'find_closest_city'
that takes a path to data file and coordinates
and returns a name of the city closest to the provided coordinates.

Use data from file pointed by cities_data_path variable
Result should be a string.
"""
from typing import Tuple

cities_data_path = r"data\cities.json"


# Your solution here
def find_closest_city(path: str, coordinates: Tuple[float, float]) -> str:
    pass


if __name__ == '__main__':
    test_coordinates = (50.103611, 19.315556)
    result = find_closest_city(path=cities_data_path, coordinates=test_coordinates)
    print(result)
