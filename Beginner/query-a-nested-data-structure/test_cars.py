from copy import deepcopy
import pytest

from cars import (
    cars,
    get_all_jeeps,
    get_first_model_each_manufacturer,
    get_all_matching_models,
    sort_car_models,
)


@pytest.fixture(name="cars")
def cars_dict():
    return deepcopy(cars)


def test_get_all_jeeps(cars):
    expected = "Grand Cherokee, Cherokee, Trailhawk, Trackhawk"
    actual = get_all_jeeps(cars)
    assert isinstance(actual, str)
    assert actual == expected


def test_get_first_model_each_manufacturer(cars):
    actual = get_first_model_each_manufacturer(cars)
    expected = ["Falcon", "Commodore", "Maxima", "Civic", "Grand Cherokee"]
    assert actual == expected


def test_get_all_matching_models_default_grep(cars):
    expected = ["Trailblazer", "Trailhawk"]
    assert get_all_matching_models(cars) == expected


def test_get_all_matching_models_different_grep(cars):
    expected = ["Accord", "Commodore", "Falcon"]
    assert get_all_matching_models(cars, grep="CO") == expected


def test_sort_dict_alphabetically(cars):
    actual = sort_car_models(cars)
    # Order of keys should not matter, two dicts are equal if they have the
    # same keys and the same values.
    # The car models (values) need to be sorted here though
    expected = {
        "Ford": ["Fairlane", "Falcon", "Festiva", "Focus"],
        "Holden": ["Barina", "Captiva", "Commodore", "Trailblazer"],
        "Honda": ["Accord", "Civic", "Jazz", "Odyssey"],
        "Jeep": ["Cherokee", "Grand Cherokee", "Trackhawk", "Trailhawk"],
        "Nissan": ["350Z", "Maxima", "Navara", "Pulsar"],
    }
    assert actual == expected