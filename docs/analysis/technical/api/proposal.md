[Index](../../../../README.md) > [Technical analysis](../README.md) > [API](README.md) > Proposal API

# Proposal API

![](https://img.shields.io/badge/GET-informational?style=flat) /api/v1/question/{question_id}/proposals *Get the list of proposal*

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

![](https://img.shields.io/badge/POST-informational?style=flat&color=2bbc8a) /api/v1/question/{question_id}/proposals *Posts a new proposal*

#### Parameters

| Name | Description |
| - | - |
| **question_id** *required ||
| **label** *required ||

#### Responses

| Code | Description |
| - | - |
| 200 | Request executed successfully |
| 400 | Not a JSON |
| 400 | Missing label |
| 404 | Question not found |
| 401 | Unauthorized |
| 498 | Token expired/invalid |

![](https://img.shields.io/badge/DELETE-informational?style=flat&color=ff0000) /api/v1/proposals/{proposal_id} *Deletes a proposal based on the id provided*

#### Parameters

| Name | Description |
| - | - |
| **proposal_id** *required ||

#### Responses

| Code | Description |
| - | - |
| 200 | Request executed successfully |
| 400 | Not a JSON |
| 404 | Proposal not found |
| 401 | Unauthorized |
| 498 | Token expired/invalid |

![](https://img.shields.io/badge/PUT-informational?style=flat&color=fc9003) /api/v1/proposals/{proposal_id} *Updates the proposal info based on the id provided*

#### Parameters

| Name | Description |
| - | - |
| **proposal_id** *required ||

#### Responses

| Code | Description |
| - | - |
| 200 | Request executed successfully |
| 400 | Not a JSON |
| 404 | Proposal not found |
| 401 | Unauthorized |
| 498 | Token expired/invalid |

![](https://img.shields.io/badge/GET-informational?style=flat) /api/v1/proposals/{proposal_id} *Retrieves a question based on ip provided*

#### Parameters

| Name | Description |
| - | - |
| **proposal_id** *required ||

#### Responses

| Code | Description |
| - | - |
| 200 | Request executed successfully |
| 404 | Proposal not found |
| 401 | Unauthorized |
| 498 | Token expired/invalid |

---
###### 2021 - SurveyStorm
