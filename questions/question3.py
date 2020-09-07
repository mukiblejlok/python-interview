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
cities_data_path = r"data\cities.json"


# Your solution here
def check_if_higher(path: str, city1: str, city2: str) -> bool:
    pass


if __name__ == '__main__':
    # Is Krakow elevated higher than Katowice?
    is_kra_higher = check_if_higher(path=cities_data_path, city1="Krakow", city2="Katowice")
    print(is_kra_higher)
