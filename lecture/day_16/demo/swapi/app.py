import requests
from pprint import pprint


res = requests.get("https://swapi.dev/api/people/1/")

data = res.json()
