[Index](../../../../README.md) > [Technical analysis](../README.md) > [API](README.md) > Question API

# Question API

![](https://img.shields.io/badge/GET-informational?style=flat) /api/v1/surveys/{survey_id}/questions *Get the list of questions*

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

![](https://img.shields.io/badge/POST-informational?style=flat&color=2bbc8a) /api/v1/{survey_id}/questions *Post a new question*

#### Parameters

| Name | Description |
| - | - |
| **survey_id** *required ||
| **label** *required ||

#### Responses

| Code | Description |
| - | - |
| 200 | Request executed successfully |
| 400 | Not a JSON |
| 400 | Missing label |
| 404 | Survey not found |
| 401 | Unauthorized |
| 498 | Token expired/invalid |

![](https://img.shields.io/badge/DELETE-informational?style=flat&color=ff0000) /api/v1/questions/{question_id} *Deletes a question based on the id provided*

#### Parameters

| Name | Description |
| - | - |
| **question_id** *required ||

#### Responses

| Code | Description |
| - | - |
| 200 | Request executed successfully |
| 400 | Not a JSON |
| 404 | Question not found |
| 401 | Unauthorized |
| 498 | Token expired/invalid |

![](https://img.shields.io/badge/PUT-informational?style=flat&color=fc9003) /api/v1/questions/{question_id} *Updates the question info based on the id provided*

#### Parameters

| Name | Description |
| - | - |
| **question_id** *required ||

#### Responses

| Code | Description |
| - | - |
| 200 | Request executed successfully |
| 404 | Question not found |
| 401 | Unauthorized |
| 498 | Token expired/invalid |

![](https://img.shields.io/badge/GET-informational?style=flat) /api/v1/questions/{question_id} *Retrieves a question based on ip provided*

#### Parameters

| Name | Description |
| - | - |
| **question_id** *required ||

#### Responses

| Code | Description |
| - | - |
| 200 | Request executed successfully |
| 404 | Question not found |
| 401 | Unauthorized |
| 498 | Token expired/invalid |
