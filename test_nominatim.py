import pytest
import requests
from services import get_accurate_coords, into_list, get_name, get_name_via_coords
import os
from data.invalid_data import NEGATIVE_PARAMS_FORWARD, NEGATIVE_PARAMS_REVERSED, EXAMPLE_URL1, NEGATIVE_FORMATS
from data_generators import SEARCH_API, REVERSED_API


data = os.path.join('data/data.json')


@pytest.mark.parametrize('place', into_list(data))
class TestForwardGeo:

    """Тест на совпадение имен"""
    def test_positive_scenario(self, place):
        assert place['display_name'] in get_name(place['display_name']), \
            f"Имена {place['display_name']} и {get_name(place['display_name'])} немного отличаются друг от друга"

    """Тест на точнейшее соответствие сгенерированных мест изначальным координатам"""
    def test_accurate_semipositive_scenario(self, place):
        assert (place['lat'], place['lon']) == (get_accurate_coords(place['display_name'])),\
            f"{place['lat'], place['lon']} незначительно отличаются {get_accurate_coords(place['display_name'])}"


@pytest.mark.parametrize('place', into_list(data))
class TestReversedGeo:

    """Тест на проверку сходится ли название мест по координатам"""
    def test_positive_scenario(self, place):
        assert place['display_name'] == get_name_via_coords(place['lat'], place['lon']), \
            f"Названия {place['display_name']} и {get_name_via_coords(place['lat'], place['lon'])} немного отличаются друг от друга"


class TestNegativeParams:

    @pytest.mark.xfail
    @pytest.mark.parametrize('actual, expected', NEGATIVE_PARAMS_FORWARD)
    def test_negative_scenario1(self, actual, expected):
        response = requests.get(SEARCH_API, params=actual)
        actual_location = response.json()[0]['display_name']
        assert actual_location == expected, 'Invalid params'

    @pytest.mark.xfail
    @pytest.mark.parametrize('actual, expected', NEGATIVE_PARAMS_REVERSED)
    def test_negative_scenario2(self, actual, expected):
        response = requests.get(REVERSED_API, params=actual)
        actual_location = response.json()[0]['display_name']
        assert actual_location == expected, 'Invalid params'

    @pytest.mark.xfail
    @pytest.mark.parametrize('format', NEGATIVE_FORMATS)
    def test_negative_formats(self, format):
        url = requests.get(EXAMPLE_URL1, params=format)
        print(url.status_code)
        assert url.status_code == 200, 'Invalid Format'


