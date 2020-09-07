"""
Question

Find name of the city which is closest to Libiąż (50.103611, 19.315556)

Use data from file pointed by cities_data_path variable
Result should be a string assigned to variable 'answer2'.
"""
from questions.helpers.paths import cities_data_path

# Your solution here
import json

from questions.helpers.distance import calculate_distance

with open(cities_data_path) as f:
    cities = json.load(f)

lib_lat, lib_lng = 50.103611, 19.315556

closest_city = None
shortest_distance = float("inf")
for city in cities:
    distance = calculate_distance(lat1=lib_lat,
                                  lng1=lib_lng,
                                  lat2=float(city.get("lat")),
                                  lng2=float(city.get("lng")))
    if distance < shortest_distance:
        closest_city = city.get("city")
        shortest_distance = distance

# Your answer here
answer2 = closest_city

if __name__ == '__main__':
    print(answer2)
