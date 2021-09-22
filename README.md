# `<PROJECT NAME>`

<!--
SurveyStorm - surveystorm.io
MassSurvey - MassSurvey.io
SurveyLab - SurveyLab.io
SurveyHack - SurveyHack.io
SurveyPool - SurveyPool.io
SurveyTrack - SurveyTrack.io
SurveyMind - SurveyMind.io
Surveyocity - Surveyocity.io
DesignSurvey - DesignSurvey.io 
-->

## Introduction

### `<PROJECT NAME>` provide an API that manages survey creation, edition and statistics, and allows users to answers an enabled survey.

## Team

### [Nathan LAPEYRE](https://github.com/Sarolus) (API Development)

He likes back & worships tests.

### [Simon BRARD](https://github.com/SimonBr017) (Web back & front development)

He only swears by HTML/CSS.

### [Adrien MILLOT](https://github.com/adrienmillot) (Mobile back & front development)

If you're not mobile you're stuck.

## Technologies

### [![](https://img.shields.io/badge/python-informational?style=flat&logo=python&logoColor=white)](https://www.python.org)

**option** : Ruby

> Ruby concerns a smaller population of developper than python and has a lesser range of libraries. Python supporting multiple inheritance is one of the main characteristics we are searching for, and the use of dictionnary type in python is quite a bonus for JSON data format.

### [![](https://img.shields.io/badge/flask-informational?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/en/2.0.x/)

**option** : Rails

> Rails works with Ruby language. Developers are more confortable and have more experience with Python language.

### [![](https://img.shields.io/badge/swift-informational?style=flat&logo=swift&logoColor=white)](https://swift.org)

**option**: flutter

> You don’t always need to use the platform-native solution to create a successful application even if you think about widening your offer and delivering the same application on other platforms. In our case, we will do it only for one. So the IDE could be the explanation to choose. And XCode is better than VSCode for that.

## Challenge

The goal of this project is to provide a tool that will help people working in the scientific and in the survey fields by letting them build custom surveys. Using database storage for the survey data and statistics that will be calculated by `<PROJECT NAME>`. This tool will be accessible to everyone, and the intent is to be able to use it everywhere, from web or mobile.

## Risks

### Technical risks

| Level | Risk | safeguards or alternatives |
| ----- | ---- | -------------------------- |
|       | Not finding enough documentation | Ask to cohort 13 |

### Non-technical risks

| Level | Risk | safeguards or alternatives |
| ----- | ---- | -------------------------- |
|   ![](https://img.shields.io/badge/16-informational?style=flat&logoColor=white&color=ff0000)  |Underestimating the competence of a colleague | |
|   ![](https://img.shields.io/badge/15-informational?style=flat&logoColor=white&color=ff4603)   | Underestimating the difficulty of a task | Set up a `Planning poker`(Scrum method) |
|   ![](https://img.shields.io/badge/10-informational?style=flat&logoColor=white&color=ff8103)   | Abandon a colleague | Set up a `Daily`(Scrum method) |

## Infrastructure

### Schema

- Basic infrastructure

![basic infra](./docs/images/basic_infra.png)

- Optimal infrastructure

![optimized infra](./docs/images/optimized_infra.png)

### Database server

One server to persist data. We can duplicate it and use another one to secure them.

### Application server

We need two application server (python is interpreted language). One for the API, and another one for the web.

We use this configuration to be as closer as possible t productivity.

### Web server

We use two Web servers, one server for the mobile application and one server for the web application. 

In the long term potantially four servers could be used, two for the Web app and two for the mobile app, moderate by two loads balancers.

## Existing Solutions

| Order | Name |
| - | - |
| ![](https://img.shields.io/badge/1-informational?style=flat) | [Survey Monkey](https://www.surveymonkey.com/)
| ![](https://img.shields.io/badge/2-informational?style=flat) | [SoGoSurvey](https://www.sogosurvey.com/) |
|   | [Typeform](https://www.typeform.com/surveys/) |
|   | [Google Forms](https://docs.google.com/forms/u/0/) |
|   | [Client Heartbeat](https://www.clientheartbeat.com/) |
|   | [Zoho Survey](https://www.zoho.com/fr/survey/) |
|   | [Survey Gizmo](https://www.alchemer.com/) |
|   | [Survey Planet](https://surveyplanet.com/) |
