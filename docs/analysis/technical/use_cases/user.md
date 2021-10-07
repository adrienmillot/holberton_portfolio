[Index](../../../../README.md) > [Technical analysis](../README.md) > [Use cases](README.md) > User use cases

# User use cases

## Create a user

User is defined by an `id` (UUID), an `username` (string(256)), a `password` (string(256)), `created_at` (datetime), `updated_at` (datetime) and `deleted_at` (datetime).

- The `id` will automatically defined by the API.
- The `created_at` is automatically defined, required.
- The `updated_at` is automatically defined, required.
- The `deleted_at` is automatically defined to null, required.
- The `username` is unique, required.
- The `password` is unique, required.

> Password is encrypted before to store it in the database.

User is also defined by a Profile. This one is defined by a `lastname` (string(256)), a `firstname` (string(256)), `gender` (string(256)) and a `born_at` (datetime).

An user could be created only by an admin user.

## Show a user

- An user is defined by the `lastname` and the `firstname` (if it is not noticed use `username`).

- An user is defined by own top survey's statistics.

- An user is defined by own worst survey's statistics.

- An user is defined by own top category's statistics.

- An user is defined by own worst category's statistics.

An user can be edited.
An user can be disabled.

## Update a user

User is defined by an `id` (UUID), an `username` (string(256)), a `password` (string(256)) and `updated_at` (datetime).

- The `id` will automatically defined by the API.
- The `username` is unique, required.
- The `password` is unique, required.
- The `updated_at` is automatically defined, required.

User is also defined by a Profile. This one is defined by a `lastname` (string(256)), a `firstname` (string(256)), `gender` (string(256)) and a `born_at` (datetime).

An user could be updated only by an admin user.

## Delete a user

A survey could be disabled only by an admin user.

To disable a survey we indicate the suppress date (`deleted_at`).

## List users

We don't list all user in one shot. We cut the list to present a part of the results.
The user'list display use the scroll or a pagination to get more users.
Only user's `lastname` and `firstname` is displayed (or `username` if there are not defined).
We can edit or disabled a user from the list.

## Authenticate

Each entrypoints of the API should be secure. Only members could use them.

To be authenticated, `username` and `password` should match.
When the match is proven, a token is generated and store in the database with a time limit, and returned.

## Logout

In the second step, an user will be automatically logout after `<NUMBER TO DETERMINE>` minutes.

He can logout by himself.

---
###### 2021 - SurveyStorm
