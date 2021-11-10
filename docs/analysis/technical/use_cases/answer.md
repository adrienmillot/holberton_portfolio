[Index](../../../../README.md) > [Technical analysis](../README.md) > [Use cases](README.md) > Answer use cases

# Answer use cases

## Create an answer

Answer is defined by an `user_id` (UUID), a `question_id` (UUID), a `proposal_id` (UUID), `created_at` (datetime), `updated_at` (datetime) and `deleted_at` (datetime).

- The `user_id` is required.
- The `question_id` is required.
- The `proposal_id` is required.
- The `created_at` is automatically defined, required.
- The `updated_at` is automatically defined, required.
- The `deleted_at` is automatically defined to null, required.

An answer could be created only by an user.

## Update an answer

Answer is defined by an `proposal_id` (UUID) and `updated_at` (datetime).

- The `proposal_id` is unique, required.
- The `updated_at` is automatically defined, required.

An answer could be updated only by an admin user.
