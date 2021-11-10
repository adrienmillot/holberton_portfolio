[Index](../../../../README.md) > [Technical analysis](../README.md) > [Use cases](README.md) > Question use cases

# Question use cases

## Create a question

Question is defined by an `id` (UUID), a `label` (string(256)), `created_at` (datetime), `updated_at` (datetime) and `deleted_at` (datetime).

- The `id` will automatically defined by the API.
- The `created_at` is automatically defined, required.
- The `updated_at` is automatically defined, required.
- The `deleted_at` is automatically defined to null, required.
- The `label` is unique, required.

A question could be created only by an admin user.

In a first step, question creation can't create proposal in the same step.

## Show a question

- A question is defined by the `label`.

- A question is defined by question's statistics (for everybody - number of good answer).

- A question is defined by question's statistics (for user).

A question can be edited.
A question can be disabled.

## Update a question

Question is defined by an `id` (UUID), a `label` (string(256)) and `updated_at` (datetime).

- The `label` is unique, required.
- The `updated_at` is automatically defined, required.

A question could be updated only by an admin user.

In a first step, question update step can't create/update proposal in the same step.

## Delete a question

A question could be disabled only by an admin user.

To disable a question we indicate the suppress date (`deleted_at`).

## List questions

We don't list all question in one shot. We cut the list to present a part of the results.
The question'list display use the scroll or a pagination to get more question.
Only question `label` is displayed.
We can edit or disabled a question from the list.

---
###### 2021 - SurveyStorm
