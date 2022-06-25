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
        # Make a new dict and return specific data
        languages = response.get("languages")
        languages = list(languages.values())
        return languages
    else:
        raise Exception("Error api call")
