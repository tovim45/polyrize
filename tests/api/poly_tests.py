import pytest

from tests.api.data_json_body import json_body
from tests.api.poly_api import get_list_of_poly_data, get_poly_data, delete_poly_data, created_object, \
    get_token_negative_test, auth_json


@pytest.fixture(scope="function")
def set_up():
    print("set_up-fixture")


def test_get_list_of_poly_data(set_up):
    print("Test get list of all poly data")
    print(get_list_of_poly_data())


@pytest.mark.parametrize("object_id", [5, 6])
def test_get_poly_data(set_up, object_id):
    print("Test get poly data by object_id")
    print(get_poly_data(object_id))


def test_delete_poly_dataa(set_up):
    print("Test delete poly data by object_id")
    print(delete_poly_data(2))


def test_created_object():
    print("Test created object read data from json file data_json_body.py")
    for data in json_body:
        print(data)
        assert created_object(data) == 200


def test_created_object_empty_body():
    print("Test created object with empty_body response code = 400")
    json = {}
    assert created_object(json) == 400


def test_get_token_negative_test_empty_json():
    print("Test get_token_negative_test empty json response code = 401")
    json = {}
    assert get_token_negative_test("http://localhost:8000/api/auth", json) == 401


def test_get_token_negative_test_wrong_url():
    print("Test get_token_negative_test wrong url response code = 500")
    assert get_token_negative_test("http://localhost:8000/api", auth_json) == 500
