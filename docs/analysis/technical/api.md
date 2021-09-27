[Index](../../README.md) > [Technical analysis](README.md) > API documentation

# API documentation

## Survey

![](https://img.shields.io/badge/GET-informational?style=flat) /api/v1/surveys *Get the list of surveys*

#### Parameters

No parameters

#### Responses

| Code | Description |
| - | - |
| 200 | Request executed successfully |

![](https://img.shields.io/badge/POST-informational?style=flat&color=2bbc8a) /api/v1/surveys *Post a new survey*

#### Parameters

| Name | Description |
| - | - |
| **survey_id** *required ||
| **name** *required ||

#### Responses

| Code | Description |
| - | - |
| 200 | Request executed successfully |
| 400 | Not a JSON |
| 400 | Missing survey_id |
| 400 | Missing name |

![](https://img.shields.io/badge/DELETE-informational?style=flat&color=ff0000) /api/v1/surveys/{survey_id} *Deletes a survey based on the id provided*

#### Parameters

| Name | Description |
| - | - |
| **survey_id** *required ||

#### Responses

| Code | Description |
| - | - |
| 200 | Request executed successfully |
| 404 | Not found |

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
| 404 | Not found |

![](https://img.shields.io/badge/GET-informational?style=flat) /api/v1/surveys/{survey_id} *Retrieves a survey based on id provided*

#### Parameters

| Name | Description |
| - | - |
| **survey_id** *required ||

#### Responses

| Code | Description |
| - | - |
| 200 | Request executed successfully |
| 404 | Not found |

## Question

![](https://img.shields.io/badge/GET-informational?style=flat) /api/v1/questions *Get the list of questions*

![](https://img.shields.io/badge/POST-informational?style=flat&color=2bbc8a) /api/v1/questions *Post a new question*

![](https://img.shields.io/badge/DELETE-informational?style=flat&color=ff0000) /api/v1/questions/{question_id} *Deletes a question based on the id provided*

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
| 404 | Missing not found |

![](https://img.shields.io/badge/PUT-informational?style=flat&color=fc9003) /api/v1/questions/{question_id} *Updates the question info based on the id provided*

#### Parameters

| Name | Description |
| - | - |
| **question_id** *required ||

#### Responses

| Code | Description |
| - | - |
| 200 | Request executed successfully |
| 400 | Not a JSON |
| 404 | Not found |

![](https://img.shields.io/badge/GET-informational?style=flat) /api/v1/questions/{question_id} *Retrieves a question based on ip provided*

#### Parameters

| Name | Description |
| - | - |
| **question_id** *required ||

#### Responses

| Code | Description |
| - | - |
| 200 | Request executed successfully |
| 404 | Not found |

## Proposal

![](https://img.shields.io/badge/GET-informational?style=flat) /api/v1/proposals *Get the list of proposal*

![](https://img.shields.io/badge/POST-informational?style=flat&color=2bbc8a) /api/v1/proposals *Posts a new proposal*

![](https://img.shields.io/badge/DELETE-informational?style=flat&color=ff0000) /api/v1/proposals/{proposal_id} *Deletes a proposal based on the id provided*

#### Parameters

| Name | Description |
| - | - |
| **proposal_id** *required ||
| **label** *required ||

#### Responses

| Code | Description |
| - | - |
| 200 | Request executed successfully |
| 400 | Not a JSON |
| 404 | Not found |

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
| 404 | Not found |

![](https://img.shields.io/badge/GET-informational?style=flat) /api/v1/proposals/{proposal_id} *Retrieves a question based on ip provided*

#### Parameters

| Name | Description |
| - | - |
| **proposal_id** *required ||

#### Responses

| Code | Description |
| - | - |
| 200 | Request executed successfully |
| 404 | Not found |

## User

![](https://img.shields.io/badge/GET-informational?style=flat) /api/v1/users *Get the list of user*

![](https://img.shields.io/badge/POST-informational?style=flat&color=2bbc8a) /api/v1/users *Posts a new user*

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
| 404 | Not found |

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
| 404 | Not found |

![](https://img.shields.io/badge/GET-informational?style=flat) /api/v1/users/{user_id} *Retrieves an user based on ip provided*

#### Parameters

| Name | Description |
| - | - |
| **user_id** *required ||

#### Responses

| Code | Description |
| - | - |
| 200 | Request executed successfully |
| 404 | Not found |

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
| 404 | Not found |

## Category

![](https://img.shields.io/badge/GET-informational?style=flat) /api/v1/categories *Get the list of category*

![](https://img.shields.io/badge/POST-informational?style=flat&color=2bbc8a) /api/v1/categories *Posts a new category*

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
| 404 | Not found |

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
| 404 | Not found |

![](https://img.shields.io/badge/GET-informational?style=flat) /api/v1/categories/{category_id} *Retrieves a category based on ip provided*

#### Parameters

| Name | Description |
| - | - |
| **category_id** *required ||

#### Responses

| Code | Description |
| - | - |
| 200 | Request executed successfully |
| 404 | Not found |

---
###### 2021 - SurveyStorm
