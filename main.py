#!/opt/anaconda3/bin/python
import requests
from datetime import datetime
from dotenv import load_dotenv
import os
import csv

load_dotenv() # loads auth key from .env file
AUTH_KEY = os.environ.get("AUTH_KEY")
DATA_PATH = os.environ.get("DATA_PATH")

def get_response():
    url = "https://api.density.io/v2/displays/dsp_956223069054042646"
    headers = {
        "Authorization": AUTH_KEY
    }

    response = requests.get(url, headers=headers)

    data = response.json()
    current_capacity = data["dedicated_space"]["current_count"]
    max_capacity = data["dedicated_space"]["capacity"]
    
    return current_capacity, max_capacity


if __name__ == "__main__":
    dt = datetime.now()
    date = dt.strftime("%Y-%m-%d")
    time = dt.strftime("%H:%M:%S")
    day = dt.strftime("%A")
    current_capacity, max_capacity = get_response()
    
    data = [date, time, day, current_capacity, max_capacity, current_capacity/max_capacity*100]
    print(data)

    # append data to csv
    with open(DATA_PATH, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data)
        file.close()
        
