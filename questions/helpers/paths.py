import os
from dotenv import load_dotenv

load_dotenv()

_this_dir = os.path.dirname(os.path.abspath(__file__))
path_to_data_folder = os.path.join(_this_dir, os.pardir, os.pardir, "data")
cities_data_path = os.path.join(path_to_data_folder, "cities.json")
