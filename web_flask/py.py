#!/usr/bin/python3
"""Use Reddit API to get data"""
import requests
import json



def login():
    """log"""

    url = 'http://0.0.0.0:5001/api/v1/auth/login'
    header = {"Content-Type": 'application/json'}
    user_info = { "username": "toto", "password": "toto" }
    json_data = json.dumps(user_info)
    
    request = requests.post(url,  json_data, headers=header)

    if request.status_code == 400:
        print('error 400')
        print(request.json())
        return (0)
    print("success!")
    print(request.json())
    print(request.json().get("auth_token"))
    
    token = request.json().get("auth_token")
    url2 = 'http://0.0.0.0:5001/api/v1/profiles'
    header2 = { 'Authorization': 'Bearer '+token}
    
    request= requests.get(url2, headers=header2)
    
    if request.status_code != 200:
        print('error')
        print(request.json())
    print('2nd success')
    print(request.json())
    
    return 0

if __name__ == '__main__':
    login()    
