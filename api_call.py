import json
import os

import requests
from dotenv import find_dotenv, load_dotenv

# Load enviroment
load_dotenv(find_dotenv(filename=os.path.join(os.getcwd(), ".env")))

def make_restcountries_call(name_countrie):
    """  
        Make call to API REST COUNTRIES v3
    """
    url = os.getenv("API_URL") + name_countrie
    response = requests.get(url) #Make request by get method
    if response.status_code == 200: # Validate status code
        response = json.loads(response.text)[0] # Convert str to dict
        data = {
            "region":response.get("region"),
            "city_name":response.get("name").get("common"),
            "languages":list(response.get("languages").values())
        }
        return data
    else:
        raise Exception("\n\n\t**ALERT:error api call**\n\n")

# make_restcountries_call("angola")