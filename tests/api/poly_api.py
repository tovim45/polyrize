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


def get_list_of_poly_data():
    headers = {'Authorization': get_token(200), 'Content-Type': 'application/json'}
    uri = base_url + "/api/poly"
    return requests.get(uri, headers=headers).json()


def created_object(json_body):
    # json_body = {
    #     "object_id": 0,
    #     "data": [
    #         {
    #             "key": "key14",
    #             "val": "val4",
    #             "valType": "str14"
    #         }
    #     ]
    # }
    headers = {'Authorization': get_token(200), 'Content-Type': 'application/json'}
    uri = base_url + "/api/poly"
    resp = requests.post(uri, headers=headers, json=json_body)
    data = resp.json()
    print(data)


def get_poly_data(object_id):
    """
    get poly data by object_id
    :param object_id:
    :return: object_id - 1
    """
    headers = {'Authorization': get_token(200), 'Content-Type': 'application/json'}
    uri = base_url + "/api/poly"
    return requests.get(uri, headers=headers).json()[object_id - 1]['data']


def delete_poly_data(object_id):
    headers = {'Authorization': get_token(200), 'Content-Type': 'application/json'}
    uri = base_url + "/api/poly"
    resp = requests.delete(uri, headers=headers, data={'object_id': object_id})
    data = resp.json()
    return data


# print(get_list_of_poly_data())
# created_object()
# print(get_poly_data(5))
# print(get_poly_data(6))
# delete_poly_data(2)
