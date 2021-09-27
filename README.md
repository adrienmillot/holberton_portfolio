# SurveyStorm

## Introduction

### SurveyStorm provide an API that manages survey creation, edition and statistics, and allows users to answers an enabled survey.

## Team

### [Nathan LAPEYRE](https://github.com/Sarolus) (API Development)

> He likes back & worships tests.

### [Simon BRARD](https://github.com/SimonBr017) (Web back & front development)

> He only swears by HTML/CSS.

### [Adrien MILLOT](https://github.com/adrienmillot) (Mobile back & front development)

> If you're not mobile you're stuck.

## Technologies

### [![](https://img.shields.io/badge/python-informational?style=flat&logo=python&logoColor=white)](https://www.python.org)

**option** : Ruby

> Ruby concerns a smaller population of developer than python and has a lesser range of libraries. Python supporting multiple inheritance is one of the main characteristics we are searching for, and the use of dictionnary type in python is quite a bonus for JSON data format.

### [![](https://img.shields.io/badge/flask-informational?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/en/2.0.x/)

**option** : Rails

> Rails works with Ruby language. Developers are more confortable and have more experience with Python language.

### [![](https://img.shields.io/badge/swift-informational?style=flat&logo=swift&logoColor=white)](https://swift.org)

**option**: flutter

> You don’t always need to use the platform-native solution to create a successful application even if you think about widening your offer and delivering the same application on other platforms. In our case, we will do it only for one. So the IDE could be the explanation to choose. And XCode is better than VSCode for that.

## Challenge

The goal of this project is to provide a tool that will help people working in the scientific and in the survey fields by letting them build custom surveys. Using database storage for the survey's data and statistics that will be calculated by SurveyStorm. This tool will be accessible to everyone, and the intent is to be able to use it everywhere, from web or mobile.

## Risks

### Technical risks

| Level | Risk | safeguards or alternatives |
| ----- | ---- | -------------------------- |
|       | Not finding enough documentation | Ask to cohort 13 |

### Non-technical risks

| Level | Risk | safeguards or alternatives |
| ----- | ---- | -------------------------- |
|   ![](https://img.shields.io/badge/16-informational?style=flat&logoColor=white&color=ff0000)  |Underestimating the colleague's skills | |
|   ![](https://img.shields.io/badge/15-informational?style=flat&logoColor=white&color=ff4603)   | Underestimating the difficulty of a task | Set up a `Planning poker`(Scrum method) |
|   ![](https://img.shields.io/badge/10-informational?style=flat&logoColor=white&color=ff8103)   | Abandon a colleague | Set up a `Daily`(Scrum method) |

## Deployment strategy

## Branching workflow

We count to use [![](https://img.shields.io/badge/gitflow-informational?style=flat&logo=gitflow&logoColor=white&color=2bbc8a)](https://danielkummer.github.io/git-flow-cheatsheet/) process, then:

- **main branch**: to production features
- **develop branch**: to test features
- **feature branch**: to development features

Each pull-request on main and develop branch have to be reviewed by two other developers.

## Continuous integration

To ensure a certain parity of our code, we intend to use unit tests with ![unittest](https://img.shields.io/badge/unittest-informational?style=flat&logo=unittest&logoColor=white&color=2bbc8a).

To continue with that precision, we intend to implement ![unittest](https://img.shields.io/badge/github_actions-informational?style=flat&logo=github_actions&logoColor=white&color=2bbc8a) to ensure us each pull-request will respect this tests.

## Evolutions workflow

![Workflow](./docs/images/workflow.png)

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

We use this configuration to be as close as possible to productivity.

### Web server

We use two Web servers, one server for the mobile application and one server for the web application. 

In the long term potentially four servers could be used, two for the Web app and two for the mobile app, moderate by two loads balancers.

## Existing Solutions

| Order | Name | Similarities | Differences |
| - | - | - | - |
| ![](https://img.shields.io/badge/1-informational?style=flat) | [Survey Monkey](https://www.surveymonkey.com/) | Unlimited surveys & questions, export data (ex. .csv), Mobile App | Statistics, Branch questions
| ![](https://img.shields.io/badge/2-informational?style=flat) | [SoGoSurvey](https://www.sogosurvey.com/) | Unlimited surveys & questions, export data (ex. .csv), Mobile App | Statistics, Branch questions
| ![](https://img.shields.io/badge/3-informational?style=flat) | [Typeform](https://www.typeform.com/surveys/) | Unlimited surveys & questions, export data (ex. .csv), Branch questions | Statistics, Mobile App
| ![](https://img.shields.io/badge/4-informational?style=flat)  | [Survey Planet](https://surveyplanet.com/) | Unlimited surveys & questions, export data (ex. .csv), Branch questions, Mobile App | Statistics
| ![](https://img.shields.io/badge/5-informational?style=flat) | [Google Forms](https://docs.google.com/forms/u/0/) | Unlimited surveys & questions, export data (ex. .csv), Branch questions | Statistics, Mobile App
| ![](https://img.shields.io/badge/6-informational?style=flat) | [Survey Gizmo](https://www.alchemer.com/) | Unlimited surveys & questions, export data (ex. .csv) | Statistics, Branch questions, Mobile App

### Other similar solutions

- Qualaroo
- Client Heartbeat
- Zoho Survey
- ProProfs Survey Maker
