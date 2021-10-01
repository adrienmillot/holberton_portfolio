[Index](../../../../README.md) > [Technical analysis](../README.md) > [API](README.md) > User API

# User API

![](https://img.shields.io/badge/GET-informational?style=flat) /api/v1/users *Get the list of user*

#### Parameters

No parameters

#### Responses

| Code | Description |
| - | - |
| 200 | Request executed successfully |
| 401 | Unauthorized |
| 498 | Token expired/invalid |

![](https://img.shields.io/badge/POST-informational?style=flat&color=2bbc8a) /api/v1/users *Posts a new user*

#### Parameters

| Name | Description |
| - | - |
| **password** *required ||
| **username** *required ||
| **last_name** ||
| **first_name** ||
| **gender** ||
| **born_at** ||

#### Responses

| Code | Description |
| - | - |
| 200 | Request executed successfully |
| 400 | Not a JSON |
| 400 | Missing username |
| 400 | Missing password |
| 401 | Unauthorized |
| 498 | Token expired/invalid |

![](https://img.shields.io/badge/DELETE-informational?style=flat&color=ff0000) /api/v1/users/{user_id} *Deletes an user based on the id provided*

#### Parameters

| Name | Description |
| - | - |
| **user_id** *required ||
| **name** *required ||

#### Responses

| Code | Description |
| - | - |
| 200 | Request executed successfully |
| 400 | Not a JSON |
| 404 | User not found |
| 401 | Unauthorized |
| 498 | Token expired/invalid |

![](https://img.shields.io/badge/PUT-informational?style=flat&color=fc9003) /api/v1/users/{user_id} *Updates the user info based on the id provided*

#### Parameters

| Name | Description |
| - | - |
| **user_id** *required ||

#### Responses

| Code | Description |
| - | - |
| 200 | Request executed successfully |
| 400 | Not a JSON |
| 404 | User not found |
| 401 | Unauthorized |
| 498 | Token expired/invalid |

![](https://img.shields.io/badge/GET-informational?style=flat) /api/v1/users/{user_id} *Retrieves an user based on ip provided*

#### Parameters

| Name | Description |
| - | - |
| **user_id** *required ||

#### Responses

| Code | Description |
| - | - |
| 200 | Request executed successfully |
| 404 | User not found |
| 401 | Unauthorized |
| 498 | Token expired/invalid |

![](https://img.shields.io/badge/POST-informational?style=flat&color=2bbc8a) /api/v1/login *Authenticates a user*

#### Parameters

| Name | Description |
| - | - |
| **username** *required ||
| **password** *required ||

#### Responses

| Code | Description |
| - | - |
| 200 | Request executed successfully |
| 400 | Missing username |
| 400 | Missing password |
| 404 | User not found |
