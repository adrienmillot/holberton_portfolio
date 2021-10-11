#!/usr/bin/python3


from exceptions.any_result_exception import AnyResultException
from exceptions.attribute_not_found_exception import AttributeNotFoundException
from exceptions.wrong_class_exception import WrongClassException
import requests


class APIStorage:
    base_url = ""

    def all(self, cls=None, **kwargs):
        try:
            if (cls.__class__.__name__ == 'Category'):
                entrypoint = 'categories'
            elif (cls.__class__.__name__ == 'Proposal'):
                if 'question_id' not in kwargs:
                    raise AttributeNotFoundException('question_id')
                # TODO: Question entity not found
                entrypoint = 'questions/{}/proposals'.format(
                    kwargs['question_id'])
            elif (cls.__class__.__name__ == 'Question'):
                if 'survey_id' not in kwargs:
                    raise AttributeNotFoundException('survey_id')
                # TODO: Survey entity not found
                entrypoint = 'surveys/{}/questions'.format(kwargs['survey_id'])
            elif (cls.__class__.__name__ == 'Survey'):
                entrypoint = 'surveys'
            elif (cls.__class__.__name__ == 'User'):
                entrypoint = 'users'
            else:
                raise WrongClassException(cls)

            url = "https://{}/{}".format(
                self.base_url,
                entrypoint
            )
            response = requests.get(url=url)
            content = response.json()

            if (len(content) == 0):
                raise AnyResultException
        except Exception:
            return False

    def delete(self, obj=None):
        """
            Delete obj from __objects if it’s inside
        """

        try:
            if (obj.__class__.__name__ == 'Category'):
                entrypoint = 'categories/{}'.format(obj.id)
            elif (obj.__class__.__name__ == 'Proposal'):
                entrypoint = 'proposals/{}'.format(obj.id)
            elif (obj.__class__.__name__ == 'Question'):
                entrypoint = 'questions/{}'.format(obj.id)
            elif (obj.__class__.__name__ == 'Survey'):
                entrypoint = 'surveys/{}'.format(obj.id)
            elif (obj.__class__.__name__ == 'User'):
                entrypoint = 'users/{}'.format(obj.id)
            else:
                raise WrongClassException(obj)

            url = "https://{}/{}".format(
                self.base_url,
                entrypoint
            )
            response = requests.delete(url=url)
            content = response.json()

            if (len(content) == 0):
                raise AnyResultException
        except Exception:
            return False

    def get(self, cls, id):
        """
            Returns the object based on the class name and its ID, or
            None if not found
        """

        try:
            if (cls.__class__.__name__ == 'Category'):
                entrypoint = 'categories/{}'.format(id)
            elif (cls.__class__.__name__ == 'Proposal'):
                entrypoint = 'proposals/{}'.format(id)
            elif (cls.__class__.__name__ == 'Question'):
                entrypoint = 'questions/{}'.format(id)
            elif (cls.__class__.__name__ == 'Survey'):
                entrypoint = 'surveys/{}'.format(id)
            elif (cls.__class__.__name__ == 'User'):
                entrypoint = 'users/{}'.format(id)
            else:
                raise WrongClassException(cls)

            url = "https://{}/{}".format(
                self.base_url,
                entrypoint
            )
            response = requests.get(url=url)
            content = response.json()

            if (len(content) == 0):
                raise AnyResultException
        except Exception:
            return False

    def new(self, obj):
        try:
            if (obj.__class__.__name__ == 'Category'):
                entrypoint = 'categories'
                json_data = {'name': obj.name}
            elif (obj.__class__.__name__ == 'Proposal'):
                entrypoint = 'proposals'
                json_data = {'label': obj.label}
            elif (obj.__class__.__name__ == 'Question'):
                entrypoint = 'questions'
                json_data = {'label': obj.label}
            elif (obj.__class__.__name__ == 'Survey'):
                entrypoint = 'surveys'
                json_data = {'name': obj.name}
            elif (obj.__class__.__name__ == 'User'):
                entrypoint = 'users'
                json_data = {'username': obj.username,
                             'password': obj.password}
            else:
                raise WrongClassException(obj)

            url = "https://{}/{}".format(
                self.base_url,
                entrypoint
            )
            response = requests.post(url=url, json=json_data)
            content = response.json()

            if (len(content) == 0):
                raise AnyResultException
        except Exception:
            return False
