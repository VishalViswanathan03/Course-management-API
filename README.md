# API Course Management System using FastAPI

This project implements a RESTful API for managing courses, instructors, leads, comments, and related functionalities using FastAPI, SQLAlchemy, Pydantic, and Alembic. Also includes Express.js as the middleware

## Features

- **Add Instructor**: Add new instructors to the system.
- **Add Course**: Add new courses along with details such as title, start date, maximum size, and associated instructor.
- **Update Course**: Update existing course details including title, start date, maximum size, and associated instructor.
- **Register Course**: Register a lead for a course, specifying the lead's name, email, and status.
- **Update Lead**: Update lead status (Accept / Reject / Waitlist).
- **Search Leads**: Search for leads by name or email.
- **Add Comment**: Add comments for specific courses.

## Technologies Used

- **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python 3.7+.
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **Pydantic**: Data validation and settings management using Python type annotations.
- **Alembic**: Lightweight database migration tool for usage with SQLAlchemy.
- **PostgreSQL**: Open-source relational database management system.
- **uvicorn**: ASGI server implementation, using the Web Server Gateway Interface (WSGI).
- **Python-dotenv**: Library to manage environment variables.
- **express.js**: Used express.js, a minimal and flexible Node.js web application framework

## Requirements

- **Docker**: Containerization platform to package and run applications in isolated environments.

## Getting Started

1. update the `.env` file with the database connection details (if required or keep default).

2. Build and start the Docker containers:

    ```bash
    docker-compose build
    docker-compose up
    ```

3. Access pgAdmin at [http://localhost:5050/](http://localhost:5050/) to manage the PostgreSQL database.

4. Access the Swagger UI documentation of FastAPI at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to interact with the API endpoints.

5. Open a separate terminal and perform database migrations:

    ```bash
    docker-compose run app alembic revision --autogenerate -m "New Migration"
    docker-compose run app alembic upgrade head
    ```
6. Refresh the datbase in pgadmin to see the updated tables. 

## Instructions

1. API requests can be made directly thorugh the swagger ui docs for fastapi.

2. Run the server.js (express.js) separtely  as a middleware to interact with the database through the backend built with fastAPI.
    ### Intructions:

    1. **Install Dependencies**: Make sure you have Node.js and npm installed on your machine.

    2. **Navigate to Project Directory**: Open your terminal or command prompt and navigate to the directory where the `server.js` file is located.

    3. **Install Required Node Modules and run the server**: Run the following command to install the required Node.js modules:

            
       ```bash
       npm install
       node server.js
       ```

## API Endpoints

- **GET /**: Hello world message.
- **POST /add-instructor/**: Add a new instructor.
- **POST /add-course/**: Add a new course.
- **PUT /update-course/{course_id}/**: Update an existing course.
- **POST /register-course/{course_id}/**: Register a lead for a course.
- **PUT /update-lead/{lead_id}/**: Update lead status.
- **GET /search-leads/**: Search leads by name or email.
- **POST /add-comment/**: Add a comment for a course.

## Environment Variables

Ensure the following environment variables are set in the `.env` file:

- `DATABASE_URL`: PostgreSQL database URL.
- `DB_USER`: PostgreSQL username.
- `DB_PASSWORD`: PostgreSQL password.
- `DB_NAME`: PostgreSQL database name.
- `PGADMIN_EMAIL`: Email for accessing pgAdmin.
- `PGADMIN_PASSWORD`: Password for accessing pgAdmin.

## Author

- Vishal Viswanathan - [GitHub](https://github.com/VishalViswanathan03)
