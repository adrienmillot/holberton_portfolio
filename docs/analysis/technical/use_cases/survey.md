[Index](../../../../README.md) > [Technical analysis](../README.md) > [Use cases](README.md) > Survey use cases

# Survey use cases

## Create a survey

Survey is defined by an `id` (UUID), a `name` (string(256)), `created_at` (datetime), `updated_at` (datetime) and `deleted_at` (datetime).

The `id` will automatically defined by the API.
The `created_at` is automatically defined, required.
The `updated_at` is automatically defined, required.
The `deleted_at` is automatically defined to null, required.
The `name` is unique, required.

A survey could be created only by an admin user.

In a first step, survey creation can't create question and proposal in the same step.

## Show a survey

- A survey is defined by the `name`.

- A survey is defined by question's statistics (for everybody - average).

- A survey is defined by question's statistics (for user).

- A survey is defined by category's statistics (for everybody - average).

- A survey is defined by category's statistics (for user - average).

A survey can be edited.
A survey can be disabled.

## Update a survey

Survey is defined by an `id` (UUID), a `name` (string(256)) and `updated_at` (datetime).

- The `name` is unique, required.
- The `updated_at` is automatically defined, required.

A survey could be updated only by an admin user.

In a first step, survey update step can't create/update question and proposal in the same step.

## Delete a survey

A survey could be disabled only by an admin user.

To disable a survey we indicate the suppress date (`deleted_at`).

## List surveys

We don't list all survey in one shot. We cut the list to present a part of the results.
The survey'list display use the scroll or a pagination to get more surveys.
Only survey `name` is displayed.
We can edit or disabled a survey from the list.

---
###### 2021 - SurveyStorm
