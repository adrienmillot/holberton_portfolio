[Index](../../../README.md) > [Making progress](README.md) > Project updates

# Project updates

## Friday 08/10/20121 to Sunday 10/10/2021

### Implements models

- Base model : Model used to initialize common attributes for other models (id, created_at, updated_at).
- Survey model : Model used to initialize survey attributes (name).
- Question model : Model used to initialize question attributes (label).
- Category model : Model used to initialize category attributes (name).
- Proposal model : Model used to initiliaze proposal attributes (label).
- User model : Model used to initialize user attributes (username, password).
- Profile model : Model used to initialize profile attributes (last_name, first_name, gender, born_at)

Each models was included with it's proper tests.

## Monday 11/10/2021

### Initialize database

- Build common environment
- Set up development database MySQL script
- Set up permissions for development database.
- Set up test database MySQL script
- Set up permissions for test database.
- Set up mysql environment based on docker.
- Updates models attributes for Object-Relational Mapping

### Implement database storage

- Implement all() method : Return a dictionary representation of all objects from a class present in the database (or all class if not specified)
- Implement close() method : Close the current database session.
- Implement count() method : Count the number of objects currently in storage.
- Implement delete() method : Delete an object from the database.
- Implement get() method : Returns the specified object or None if not found.
- Implement new() method : Adds a new object to the database.
- Implement reload() method : Reloads data from the database.
- Implement save() method : Save all changes to the database.

Each method was included with some of it's tests.

### Implement file storage

- Implement File storage module with needed attributes (file_path, objects)

### Implement CSV file storage

- Implement save() method for CSV file storage : Save object dictionary representation in a .csv file which be named after the date of it's generation.
- Add tests for CSV file storage methods

## Tuesday 12/10/2021

### Implement JSON file storage

- Implement save() method for JSON file storage : Save object dictionary representation in a .json file which be named after the date of it's generation.

### File & database storage unittest

- Add more tests for database storage methods.
- Add tests for JSON file storage methods.

### API User entrypoints

- Implement User authentification entrypoint
- Implement list Users entrypoint
- Implement create User entrypoint
- Implement delete User entrypoint
- Implement update User entrypoint
- Implement show User entrypoint

### API Profile entrypoints

- Implement list Profiles entrypoint
- Implement create Profile entrypoint
- Implement delete Profile entrypoint
- Implement update Profile entrypoint
- Implement show Profile entrypoint

## Wednesday 13/10/2021

### Update model & storage

- Add deleted_at attribute to base model.
- Updates attribute set up.
- Implement disable() method for database storage : Disable an object in the database.
- Updates models tests.
- Fix issues generate by new implementation.

## Thursday 14/10/2021

### Web Interface

- Start web interface building

### Making progress documentation

- Add weekly challenges documentation section
- Add weekly collaboration documentation section
- Add weekly project updates documentation section
- Add weekly progress documentation section
  
### Authentification

- Fix login issues with token authentification

---
###### 2021 - SurveyStorm