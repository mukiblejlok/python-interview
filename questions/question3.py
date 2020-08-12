"""
Question

Is Krakow elevated higher than Katowice?

Use data from file: /data/cities.json

To get the elevation data use "https://elevation-api.io/"
with key taken from environmental variable "ELEVATION_API_KEY"

Result should be a bool assigned to 'answer3'.
"""

from questions import cities_data_path

# Your solution here
import json
import requests
import os

ka_lat, ka_long = 50.258415, 19.027545
kr_lat, kr_long = 50.057531, 19.980216

base_url = r" https://elevation-api.io/api/elevation"
params = {"points": f"({ka_lat},{ka_long}),({kr_lat},{kr_long})",
          "key": os.getenv("ELEVATION_API_KEY")}
response = requests.get(url=base_url, params=params, timeout=20)

if response:
    rj = json.loads(response.text)
    katowice_elevation = rj["elevations"][0]["elevation"]
    krakow_elevation = rj["elevations"][1]["elevation"]
    is_krakow_higher = krakow_elevation > katowice_elevation

# Your answer here
answer3 = is_krakow_higher
