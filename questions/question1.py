"""
Question

Find top ten biggest cities.

Use data from file pointed by cities_data_path variable
Result should be in form of a list of strings assigned to variable 'answer'.
"""
from questions import cities_data_path

# Your solution here
import json

with open(cities_data_path) as f:
    cities = json.load(f)

cities_with_pop = [c for c in cities if c.get("population")]
top_10_cities = [city.get("city") for city in sorted(cities_with_pop, key=lambda c: float(c.get("population", 0)), reverse=True)][:10]

# Your answer here
answer = top_10_cities
