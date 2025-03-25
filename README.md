# Task Management API

## Overview
This project is a Django REST Framework (DRF)-based API for task management. It allows users to create, update, and assign tasks to users, as well as retrieve tasks assigned to a specific user.

## Features
- Create, update, and list tasks
- Assign users to tasks
- Fetch tasks assigned to a particular user
- List and create users

## Technologies Used
- Python
- Django
- Django REST Framework
- SQLite (default database, can be changed to PostgreSQL/MySQL)

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Apply database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Create a superuser (optional, for admin access):
   ```bash
   python manage.py createsuperuser
   ```
5. Run the development server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Task Endpoints
- **Create Task**: `POST /tasks/`
- **List All Tasks**: `GET /tasks/all/`
- **Update Task**: `PUT /tasks/<int:pk>/update/`
- **Assign Users to Task**: `PUT /tasks/<int:pk>/assign/`

### User Endpoints
- **List & Create Users**: `GET/POST /users/`
- **Get Tasks Assigned to a User**: `GET /users/<int:user_id>/tasks/`

## Models

### User Model
- `name` (CharField)
- `email` (EmailField, unique)
- `mobile` (CharField, optional)

### Task Model
- `name` (CharField)
- `description` (TextField)
- `created_at` (DateTimeField, auto_now_add=True)
- `task_type` (CharField, optional)
- `completed_at` (DateTimeField, optional)
- `status` (CharField, choices=[pending, in_progress, completed], default='pending')
- `assigned_users` (ManyToManyField to User)

## Usage
1. Create users using `/users/` endpoint.
2. Create tasks using `/tasks/` endpoint.
3. Assign users to tasks via `/tasks/<int:pk>/assign/`.
4. Retrieve tasks assigned to a specific user using `/users/<int:user_id>/tasks/`.

## Copyright
Saksh Arora
