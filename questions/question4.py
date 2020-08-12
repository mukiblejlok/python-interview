"""
Question

Create a CitiesInfo class that is initialized with cities_data and
provides a two methods:
* bigger_than(population: int) -> List[Dict]
* closest_to(lat: float, lng: float) -> List[Dict]

Use data from file pointed by cities_data_path variable

Result should be an object of a CitiesInfo class initialized with 'cities_data_path' assigned to variable 'answer4'.
"""
from questions import cities_data_path


# Your solution here
class CitiesInfo:
    def __init__(self, path: str):
        pass


# Your answer here
answer4 = CitiesInfo(path=cities_data_path)
