#!/usr/bin/python3


from os import getenv

import requests
from models import db_storage
from models.profile import Profile
from models.user import User
import unittest


host = getenv('SS_API_HOST_API_HOST', '0.0.0.0')
port = getenv('SS_API_PORT', '5001')
version = '/v1'
api_url = 'http://{}:{}/api{}'.format(host, port, version)


WRONG_STATUS_CODE_MSG = 'Wrong status code!'
WRONG_TYPE_RETURN_MSG = 'Wrong return type return!'


class AuthenticatedRequest(unittest.TestCase):
    auth_profile = None
    auth_profile_id = None
    url = None
    auth_user = None
    auth_user_id = None

    def setUp(self) -> None:
        self.auth_profile = Profile()
        self.auth_profile_id = self.auth_profile.id
        self.auth_user = User(username='test', password='test', profile_id=self.auth_profile_id)
        self.auth_user_id = self.auth_user.id

        self.auth_profile.save()
        self.auth_user.save

        self.__test_wrong_token()
        self.__test_unauthorized_request()

    def tearDown(self) -> None:
        user = db_storage.get_from_attributes(User, id=self.auth_user_id)
        if user is not None:
            db_storage.delete(user)
            db_storage.save()

        profile = db_storage.get_from_attributes(Profile, id=self.auth_profile.id)
        if profile is not None:
            db_storage.delete(profile)
            db_storage.save()

    def __getAuthToken(self, username, password):
        auth_url = '{}/auth/login'.format(api_url)
        data = {'username': username, 'password': password}
        resp_login = requests.post(auth_url, json=data)

        return resp_login.json()['auth_token']

    def __getAuthHeaders(self, username, password):
        return {
            'Authorization': 'Bearer ' + self.__getAuthToken(username, password)
        }

    def __getWrongAuthHeaders(self):
        return {
            'Authorization': 'Bearer toto'
        }

    def __test_wrong_token(self):
        response = requests.get(url=self.url, headers=self.__getWrongAuthHeaders)
        headers = response.headers

        self.assertEqual(response.status_code, 498, WRONG_STATUS_CODE_MSG)
        self.assertEqual(
            headers['Content-Type'], 'application/json', WRONG_TYPE_RETURN_MSG)

    def __test_unauthorized_request(self):
        response = requests.get(url=self.url)
        headers = response.headers

        self.assertEqual(response.status_code, 401, WRONG_STATUS_CODE_MSG)
        self.assertEqual(
            headers['Content-Type'], 'application/json', WRONG_TYPE_RETURN_MSG)


    def get_authenticated_response(self, url=None, http_method='get', json=None, data=None):
        url = url if url is not None else self.url

        if (http_method == 'get'):
            return requests.get(url=url, headers=self.__getAuthHeaders('test', 'test'), json=json, data=data)
        elif (http_method == 'delete'):
            return requests.delete(url=url, headers=self.__getAuthHeaders('test', 'test'), json=json, data=data)
        elif (http_method == 'post'):
            return requests.post(url=url, headers=self.__getAuthHeaders('test', 'test'), json=json, data=data)
        elif (http_method == 'put'):
            return requests.put(url=url, headers=self.__getAuthHeaders('test', 'test'), json=json, data=data)
