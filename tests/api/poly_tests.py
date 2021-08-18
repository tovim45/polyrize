import pytest

from tests.api.data_json_body import json_body
from tests.api.poly_api import get_list_of_poly_data, delete_poly_data, created_object, \
    get_token_negative_test, auth_json

objects_list = []


def test_created_object():
    print("Test created object read data from json file data_json_body.py")
    for data in json_body:
        assert created_object(data) == 200
        objects = get_list_of_poly_data()[1]
        objects_list.append(objects[-1])
        print(objects_list)


def test_verify_all_added_keys_value_in_poly_data():
    print("Test verify all added keys value in poly data")
    for i in range(len(objects_list)):
        assert objects_list[i]["data"][0]["key"] == json_body[i]["data"][0]["key"]


def test_verify_all_added_vals_value_in_poly_data():
    print("Test verify all added vals value in poly data")
    for i in range(len(objects_list)):
        assert objects_list[i]["data"][0]["val"] == json_body[i]["data"][0]["val"]


def test_verify_all_added_val_types_value_in_poly_data():
    print("Test verify all added val types value in poly_data")
    for i in range(len(objects_list)):
        assert objects_list[i]["data"][0]["valType"] == json_body[i]["data"][0]["valType"]


def test_get_list_of_all_poly_data():
    print("Test get list of all poly data")
    objects = get_list_of_poly_data()[1]
    for obj in objects:
        print(obj)
    assert get_list_of_poly_data()[0] == str(200)


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


def test_delete_all_added_by_object_id_in_poly_data():
    print("Test delete all added by object id in poly data")
    for i in range(len(objects_list)):
        print(objects_list[i]["object_id"])
        assert delete_poly_data(objects_list[i]["object_id"]) == ""


def test_delete_all_poly_data_object_ids():
    print("Test delete poly data by object_id and verify that the object_id is not exists")
    objects = get_list_of_poly_data()[1]
    for obj in objects:
        print(obj["object_id"])
        assert delete_poly_data(obj["object_id"]) == ""
