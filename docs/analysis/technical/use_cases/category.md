[Index](../../../../README.md) > [Technical analysis](../README.md) > [Use cases](README.md) > Category use cases

# Category use cases

## Create a category

Category is defined by an `id` (UUID), a `name` (string(256)), `created_at` (datetime), `updated_at` (datetime) and `deleted_at` (datetime).

- The `id` will automatically defined by the API.
- The `created_at` is automatically defined, required.
- The `updated_at` is automatically defined, required.
- The `deleted_at` is automatically defined to null, required.
- The `name` is unique, required.

A category could be created only by an admin user.

## Show a category

- A category is defined by the `name`.

- A category is defined by question's statistics (for everybody - average).

- A category is defined by question's statistics (for user).

- A category is defined by category's statistics (for everybody - average).

- A category is defined by category's statistics (for user - average).

A category can be edited.
A category can be disabled.

## Update a category

Category is defined by an `id` (UUID), a `name` (string(256)) and `updated_at` (datetime).

- The `name` is unique, required.
- The `updated_at` is automatically defined, required.

A category could be updated only by an admin user.

## Delete a category

A category could be disabled only by an admin user.

To disable a category we indicate the suppress date (`deleted_at`).

## List categories

We don't list all category in one shot. We cut the list to present a part of the results.
The category'list display use the scroll or a pagination to get more surveys.
Only category `name` is displayed.
We can edit or disabled a category from the list.

---
###### 2021 - SurveyStorm
