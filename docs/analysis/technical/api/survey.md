[Index](../../../../README.md) > [Technical analysis](../README.md) > [API](README.md) > Survey API

# Survey API

![](https://img.shields.io/badge/GET-informational?style=flat) /api/v1/surveys *Get the list of surveys*

#### Parameters

No parameters

#### Responses

| Code | Description |
| - | - |
| 200 | Request executed successfully |
| 401 | Unauthorized |
| 498 | Token expired/invalid |

![](https://img.shields.io/badge/POST-informational?style=flat&color=2bbc8a) /api/v1/surveys *Post a new survey*

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

![](https://img.shields.io/badge/DELETE-informational?style=flat&color=ff0000) /api/v1/surveys/{survey_id} *Deletes a survey based on the id provided*

#### Parameters

| Name | Description |
| - | - |
| **survey_id** *required ||

#### Responses

| Code | Description |
| - | - |
| 200 | Request executed successfully |
| 404 | Survey not found |
| 401 | Unauthorized |
| 498 | Token expired/invalid |

![](https://img.shields.io/badge/PUT-informational?style=flat&color=fc9003) /api/v1/surveys/{survey_id} *Updates the survey info based on the id provided*

#### Parameters

| Name | Description |
| - | - |
| **survey_id** *required ||

#### Responses

| Code | Description |
| - | - |
| 200 | Request executed successfully |
| 400 | Not a JSON |
| 404 | Survey not found |
| 401 | Unauthorized |
| 498 | Token expired/invalid |

![](https://img.shields.io/badge/GET-informational?style=flat) /api/v1/surveys/{survey_id} *Retrieves a survey based on id provided*

#### Parameters

| Name | Description |
| - | - |
| **survey_id** *required ||

#### Responses

| Code | Description |
| - | - |
| 200 | Request executed successfully |
| 404 | Survey not found |
| 401 | Unauthorized |
| 498 | Token expired/invalid |
