import json
import requests
from data_generators import SEARCH_API, REVERSED_API


def into_list(data):
    with open(data, 'r', encoding='UTF-8') as file:
        list_data = json.load(file)
        return list_data


def get_accurate_coords(name):
    r = requests.get(SEARCH_API, params={
        'q': name,
        'format': 'jsonv2'
    })
    print(r.json()[0]['display_name'])
    return r.json()[0]['lat'], r.json()[0]['lon']


def get_name(name):
    r = requests.get(SEARCH_API, params={
        'q': name,
        'format': 'jsonv2'
    })
    return r.json()[0]['display_name']


def get_name_via_coords(lat, lon):
    r = requests.get(REVERSED_API, params={
        'lat': lat,
        'lon': lon,
        'format': 'jsonv2'
    })
    return r.json()['display_name']