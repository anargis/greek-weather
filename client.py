import requests
import urllib.parse

"""
Chech the name of the cities in the file: greek_cities.py
Assign a new city 
"""

city = "ΣΥΡΟΣ"

encoded_city = urllib.parse.quote(city)  

response = requests.get(f"http://localhost:8000/weather/{encoded_city}")
response.raise_for_status()

data = response.json()

"""
If data is a list, iterate through each weather entry 
Print all entries (4 days)

Layout: Default
"""

if isinstance(data, list):
    for day in data:
        print("------") 
        for key, value in day.items():
            print(f"{key}: {value}")
else:
    # If data is a single dict (e.g., an error), just print it
    for key, value in data.items():
        print(f"{key}: {value}")


###### Layout 1: Print only the first entry if it's a list ######

# if isinstance(data, list) and data:
#     print("------")
#     first_day = data[0]
#     for key, value in first_day.items():
#         print(f"{key}: {value}")
# else:
#     # If data is a single dict (e.g., an error), just print it
#     for key, value in data.items():
#         print(f"{key}: {value}")


###### Layout 2: Print only the first row in one line ######

# if isinstance(data, list) and data:
#     first_day = data[0]
#     line = " | ".join(f"{key}: {value}" for key, value in first_day.items())
#     print(line)
# else:
#     print("No data found or error:", data)