import requests
import json
def test_getkey():
    header = {'accept': 'application/json', 'email': 'valid_email', 'password': 'valid_password'}
    # status, result = pf.get_api_key(email, password)
    res_get = requests.get(url='https://petfriends.skillfactory.ru/api/key', headers=header)
    # assert status == 200
    # assert 'key' in result

