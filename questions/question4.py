"""
Question

Create a 'CitiesInfo' class that is initialized with path to data file and
provides a two methods:
* bigger_than(population: int) -> List[str]
  list of city names bigger than the population
* closest_to(lat: float, lng: float, n: int) -> List[str]
  list of n cities closest to the given coordinates

Use data from file pointed by cities_data_path variable

Result should be a CitiesInfo class.
"""

# Your solution here
import json
from questions.helpers.distance import calculate_distance


class CitiesInfo:
    def __init__(self, path: str):
        with open(path) as f:
            self.data = json.load(f)

    def bigger_than(self, population: int):
        result = []
        for city_data in self.data:
            city_population = city_data.get("population")

            if city_population and int(city_population) > population:
                result.append(city_data.get('city'))
        return result

    def closest_to(self, lat: float, lng: float, n: int):
        sorted_by_distance = sorted(self.data,
                                    key=lambda c: calculate_distance(lat1=float(c.get("lat")),
                                                                     lng1=float(c.get("lng")),
                                                                     lat2=lat,
                                                                     lng2=lng))
        return [c.get('city') for c in sorted_by_distance[:n]]


if __name__ == '__main__':
    cities_data_path = r"data\cities.json"
    ci = CitiesInfo(path=cities_data_path)

