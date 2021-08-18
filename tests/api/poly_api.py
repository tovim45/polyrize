import requests

base_url = "http://localhost:8000"
token_url = base_url + "/api/auth"
auth_json = {
    "username": "test",
    "password": "1234"
}


def get_token(expected_code):
    resp = requests.request("POST", token_url, json=auth_json)
    data = resp.json()
    print('status_code is: ' + str(resp.status_code))
    print(data)
    return data["access_token"]


headers = {'Authorization': 'Bearer ' + get_token(200), 'Content-Type': 'application/json'}
uri = base_url + "/api/poly"


def get_list_of_poly_data():
    resp = requests.get(uri, headers=headers)
    data = resp.json()
    return [str(resp.status_code), data]


def created_object(json_body):
    resp = requests.post(uri, headers=headers, json=json_body)
    return resp.status_code


def get_poly_data(object_id):
    """
    get poly data by object_id
    :param object_id:
    :return: object_id - 1
    """
    return requests.get(uri, headers=headers).json()[object_id - 1]['data']


def delete_poly_data(object_id):
    return requests.delete(uri + "/" + str(object_id), headers=headers).json()


def get_token_negative_test(url, json):
    return requests.request("POST", url, json=json).status_code
