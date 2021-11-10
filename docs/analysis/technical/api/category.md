[Index](../../../../README.md) > [Technical analysis](../README.md) > [API](README.md) > Category API

# Category API

![](https://img.shields.io/badge/GET-informational?style=flat) /api/v1/categories *Get the list of category*

#### Parameters

No parameters

#### Responses

| Code | Description |
| - | - |
| 200 | Request executed successfully |
| 401 | Unauthorized |
| 498 | Token expired/invalid |

![](https://img.shields.io/badge/POST-informational?style=flat&color=2bbc8a) /api/v1/categories *Posts a new category*

#### Parameters

| Name | Description |
| - | - |
| **name** *required ||

#### Responses

| Code | Description |
| - | - |
| 200 | Request executed successfully |
| 400 | Not a JSON |
| 400 | Missing name |
| 401 | Unauthorized |
| 498 | Token expired/invalid |

![](https://img.shields.io/badge/DELETE-informational?style=flat&color=ff0000) /api/v1/categories/{category_id} *Deletes a category based on the id provided*

#### Parameters

| Name | Description |
| - | - |
| **category_id** *required ||
| **name** *required ||

#### Responses

| Code | Description |
| - | - |
| 200 | Request executed successfully |
| 400 | Not a JSON |
| 404 | Category not found |
| 401 | Unauthorized |
| 498 | Token expired/invalid |

![](https://img.shields.io/badge/PUT-informational?style=flat&color=fc9003) /api/v1/categories/{category_id} *Updates the category info based on the id provided*

#### Parameters

| Name | Description |
| - | - |
| **category_id** *required ||

#### Responses

| Code | Description |
| - | - |
| 200 | Request executed successfully |
| 400 | Not a JSON |
| 404 | Category not found |
| 401 | Unauthorized |
| 498 | Token expired/invalid |

![](https://img.shields.io/badge/GET-informational?style=flat) /api/v1/categories/{category_id} *Retrieves a category based on ip provided*

#### Parameters

| Name | Description |
| - | - |
| **category_id** *required ||

#### Responses

| Code | Description |
| - | - |
| 200 | Request executed successfully |
| 404 | Category not found |
| 401 | Unauthorized |
| 498 | Token expired/invalid |

---
###### 2021 - SurveyStorm
