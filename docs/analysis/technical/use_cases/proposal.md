[Index](../../../../README.md) > [Technical analysis](../README.md) > [Use cases](README.md) > Proposal use cases

# Proposal use cases

## Create a proposal

Proposal is defined by an `id` (UUID), a `label` (string(256)), `is_valid` (boolean), `created_at` (datetime), `updated_at` (datetime) and `deleted_at` (datetime).

- The `id` will automatically defined by the API.
- The `created_at` is automatically defined, required.
- The `updated_at` is automatically defined, required.
- The `deleted_at` is automatically defined to null, required.
- The `label` is unique, required.
- The `is_valid` is default to false.

A proposal could be created only by an admin user.

## Show a proposal

- A survey is defined by the `label`, `is_valid`.

A survey can be edited.
A survey can be disabled.

## Update a proposal

Category is defined by an `id` (UUID), a `label` (string(256)), `is_valid` (boolean), and `updated_at` (datetime).

- The `label` is unique, required.
- The `updated_at` is automatically defined, required.
- The `is_valid` is default to false.

A category could be updated only by an admin user.

## Delete a proposal

A proposal could be disabled only by an admin user.

To disable a proposal we indicate the suppress date (`deleted_at`).

## List proposals

We don't list all proposal in one shot. We cut the list to present a part of the results.
The proposal'list display use the scroll or a pagination to get more proposal.
Only proposal `label` is displayed.
We can edit or disabled a proposal from the list.

---
###### 2021 - SurveyStorm
