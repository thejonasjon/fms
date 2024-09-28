# Form Management System Backend (FMS)

## Description
    This project is an API for managing forms and form responses, built using Django Rest Framework and MongoEngine with MongoDB as the database.

## Features
- Create, retrieve, update, and delete forms.

## Prerequisites
- Docker
- Docker Compose

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

4. **Access the API**:
    - The API will be available at `http://localhost:8000/`.
    - Example API endpoints:
      - `http://localhost:8000/api/forms/`: List forms.
      - `http://localhost:8000/api/forms/{id}/`: Retrieve, update, or delete a specific form.
      - `http://localhost:8000/api/responses/`: List responses.
      - `http://localhost:8000/api/responses/submit/`: Submit responses.


## Docker Setup Overview

- The **app** service runs Django using the `python manage.py runserver 0.0.0.0:8000` command inside the Docker container.
- The **mongodb** service runs MongoDB, exposed on port `27017`.


### Docker Compose Configuration

Your `docker-compose.yml` sets up two services:
- **app**: Runs the Django server and mounts your project directory for development.
- **mongodb**: MongoDB instance for storing form data and responses.

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
    In the project, development dependencies are separated into `requirements.dev.txt`. For production, dependencies are seperated in `requirements.txt`.
