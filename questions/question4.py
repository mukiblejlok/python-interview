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
cities_data_path = r"data\cities.json"


# Your solution here
class CitiesInfo:
    def __init__(self, path: str):
        pass


if __name__ == '__main__':
    ci = CitiesInfo(path=cities_data_path)

