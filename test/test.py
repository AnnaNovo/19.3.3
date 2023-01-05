import pytest
# def test1():
#     assert (1,2,3)==(1,2,4)
#
# def test2():
#     assert 2 == 2
#
# def test3():
#     assert 1 in [1,2,3]
import requests
import json


def test_add_pet():
    input_pet = {
        "id": 120,
        "category": {
            "id": 22,
            "name": "Bossik"
        },
        'name': "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 12,
                "name": "Dog"
            }
        ],
        "status": "available"
    }

    header = {'accept': 'application/json', 'Content-Type': 'application/json'}
    res_post = requests.post(url='https://petstore.swagger.io/v2/pet', data=json.dumps(input_pet), headers=header)
    print(res_post.text)
    res_json = json.loads(res_post.text)
    assert input_pet == res_json

    res_get = requests.get(url=f'https://petstore.swagger.io/v2/pet/{input_pet ["id"]}')
    assert res_get.status_code == 200
    assert json.loads(res_get.text)==input_pet

def test_findstatus():
    input_pet = {
        "id": 48,
        "category": {
            "id": 22,
            "name": "Bossik"
        },
        'name': "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 12,
                "name": "Cat"
            }
        ],
        "status": "sold"
    }
    header = {'accept': 'application/json', 'Content-Type': 'application/json'}
    requests.post(url='https://petstore.swagger.io/v2/pet', data=json.dumps(input_pet), headers=header)
    res_get = requests.get(url=f'https://petstore.swagger.io/v2/pet/findByStatus', params={'status':'sold'})

    assert res_get.status_code == 200

    assert input_pet in list(json.loads(res_get.text))
    print(list(json.loads(res_get.text)))






