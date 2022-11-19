import json
import requests
import random

SEARCH_API = 'https://nominatim.openstreetmap.org/search'
REVERSED_API = 'https://nominatim.openstreetmap.org/reverse'


"""Random 100 coordinates generator that writes data into excel file"""
def random_coords_generator(k=1):
    data_places = []
    while k < 100:
        data = requests.get(REVERSED_API, params={
            'lat': random.uniform(-85.05112878, 85.05112878),
            'lon': random.uniform(-180, 180),
            'format': 'jsonv2'
        })

        if data.json().get('error') == 'Unable to geocode':
            continue
        else:
            data_places.append({'display_name': data.json()["display_name"],
                                'name': data.json()["name"],
                                'lat': data.json()["lat"],
                                'lon': data.json()["lon"],
                                'address': data.json(),
                                })
            print(f'{k}%')
            k += 1
    with open('data/data.json', 'w', encoding="utf-8") as file:
        json.dump(data_places, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    random_coords_generator()