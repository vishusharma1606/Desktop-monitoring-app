# Monitoring App

This project is a monitoring application with a frontend and backend service. The frontend is built with Node.js and served using `http-server`, while the backend is built with Python.

## Project Structure

```
Monitoring-app/
├── backend/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── requirements.txt
│   └── server.py
├── frontend/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── package.json
│   └── index.html
└── README.md
```

## Prerequisites

- Docker
- Docker Compose

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/Monitoring-app.git
    cd Monitoring-app
    ```

2. Build and run the services using Docker Compose:
    ```sh
    docker-compose up --build
    ```

## Frontend

The frontend service is built with Node.js and served using `http-server`.

- **Dockerfile**: Defines the Docker image for the frontend service.
- **docker-compose.yml**: Configuration for running the frontend service with Docker Compose.

## Backend

The backend service is built with Python.

- **Dockerfile**: Defines the Docker image for the backend service.
- **docker-compose.yml**: Configuration for running the backend service with Docker Compose.
- **requirements.txt**: Lists the Python dependencies.
- **server.py**: The main Python application file.

## Accessing the Application

- Frontend: http://localhost:8000
- Backend: http://localhost:8081

## License

This project is licensed under the MIT License.
