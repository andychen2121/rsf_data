import requests
from dotenv import load_dotenv
import os

load_dotenv() # "AUTH_KEY"

if __name__ == "__main__":
    url = "https://api.density.io/v2/displays/dsp_956223069054042646"
    auth_key = os.environ.get("AUTH_KEY")

    headers = {
        "Authorization": auth_key
    }

    response = requests.get(url, headers=headers)

    datetime = response.json()["created_at"]
    current_capacity = response.json()["dedicated_space"]["current_count"]
    max_capacity = response.json()["dedicated_space"]["capacity"]

    print(datetime, current_capacity, max_capacity)
