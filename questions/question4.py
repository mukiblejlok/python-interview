"""
Question

Create a 'CitiesInfo' class that is initialized with path to data file and provides two methods:

* bigger_than(population: int) -> List[str]
  list of city names bigger than the population
* closest_to(lat: float, lng: float, n: int) -> List[str]
  list of n cities closest to the given coordinates

Use data from file pointed by cities_data_path variable

Result should be a CitiesInfo class.
"""

# Your solution here
import json

from questions import CITIES_FILE_PATH
from questions.helpers.distance import calculate_distance


class CitiesInfo:
    def __init__(self, path: str):
        pass

    def bigger_than(self, population: int):
        raise NotImplementedError()

    def closest_to(self, lat: float, lng: float, n: int):
        raise NotImplementedError()


if __name__ == "__main__":
    ci = CitiesInfo(path=CITIES_FILE_PATH)

