# Form Management System Backend (FMS)
- fms


## Description
    This project is an API for managing forms and form responses, built using Django Rest Framework and MongoEngine with MongoDB as the database.


## Features
- Create, retrieve, update, and delete forms.

## Prerequisites
- Docker
- Docker Compose

## Docker Setup Overview
`docker-compose.yml` have two services:

- **app**: Runs the Django server.
- **mongodb**: MongoDB instance for database.

- The **app** service runs Django using the `python manage.py runserver 0.0.0.0:8000`
- The **mongodb** service runs MongoDB, exposed on port `27017`.


## Project Setup and Running

1. **Clone the repository**:
    ```bash
    git clone https://github.com/thejonasjon/fms.git
    cd fms
    ```

2. **Create environment variables** (optional but recommended):
    Create a `.env` file at the root of the project with the following variables, or adjust the `docker-compose.yml` file directly:
    ```bash
    # .env file
    MONGO_DB_NAME=fms_db
    MONGO_DB_HOST=mongodb
    MONGO_INITDB_ROOT_USERNAME=changeme
    MONGO_INITDB_ROOT_PASSWORD=changeme
    ```

3. **Build and run the containers**:
    ```bash
    docker-compose up --build
    ```

## Run Test
    ```bash
        docker-compose run --rm app python manage.py test
    ```

## Endpoints

### Forms:
- `GET /api/forms/`: List all forms.
- `POST /api/forms/`: Create a new form.
- `GET /api/forms/{id}/`: Retrieve a specific form.
- `PUT /api/forms/{id}/`: Update a form.
- `DELETE /api/forms/{id}/`: Delete a form.

### Responses:
- `POST /api/responses/submit/`: Submit a response to a form.
- `GET /api/responses/`: Retrieve all submitted responses.


## Technologies
- **Django**: Python web framework.
- **Django Rest Framework**: API creation with Django.
- **MongoEngine**: MongoDB ORM for managing MongoDB in Django.
- **MongoDB**: NoSQL database for storing forms and responses.
- **Docker**: Containerization for environment consistency.

## Development

### Separate Dev and Production Dependencies:
    In the project, development dependencies are separated into
    - `requirements.dev.txt`. For Development
    - `requirements.txt`. For Production