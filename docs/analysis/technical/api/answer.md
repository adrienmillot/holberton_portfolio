[Index](../../../../README.md) > [Technical analysis](../README.md) > [API](README.md) > Answer API

# Answer API

![](https://img.shields.io/badge/POST-informational?style=flat&color=2bbc8a) /api/v1/question/{question_id}/proposal/{proposal_id} *Posts a new answer*

#### Parameters

| Name | Description |
| - | - |
| **question_id** *required ||
| **proposal_id** *required ||
| **user_id** *required ||

#### Responses

| Code | Description |
| - | - |
| 200 | Request executed successfully |
| 404 | Question not found |
| 404 | Proposal not found |
| 404 | User not found |
| 401 | Unauthorized |
| 498 | Token expired/invalid |

![](https://img.shields.io/badge/PUT-informational?style=flat&color=fc9003) /api/v1/question/{question_id}/proposal/{proposal_id} *Updates the category info based on the id provided*

#### Parameters

| Name | Description |
| - | - |
| **category_id** *required ||

#### Responses

| Code | Description |
| - | - |
| 200 | Request executed successfully |
| 400 | Not a JSON |
| 404 | Question not found |
| 404 | Proposal not found |
| 404 | User not found |
| 401 | Unauthorized |
| 498 | Token expired/invalid |
