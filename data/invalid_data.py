EXAMPLE_URL1 = 'https://nominatim.openstreetmap.org/search?q=Moscow'

NEGATIVE_PARAMS_FORWARD = [
    ('q=', ' '),
    ('Saint Petersburg', 'Saint Petersburg'),
    ('1235412', '1235412'),
    ('q=Rome&headers&format=json', 'Rome'),
    ('z=Moscow&format=json', 'Moscow'),
    ('cite=Moscow&format=json', 'Moscow'),
    ('postcode=Romania&format=json', 'Romania'),
]

NEGATIVE_PARAMS_REVERSED = [
    ('lat=1156,4343&lon=38,3252&format=json', ''),
    ('lat=&lon=&format=json', ''),
    ('lat=-181&format=json', ''),
    ('lat=-181&format=json', ''),
]


NEGATIVE_FORMATS = [
    'format=text/html',
    'format=yaml',
    'format=audio',
    'format=text/plain',
    'format=application',
]
