# Task Management App

Welcome to the Task Management App, a Django-based web application for managing tasks.

## Features

- **CRUD Operations**: Perform Create, Read, Update, and Delete operations for tasks.
- **User Authentication**: Secure login and authentication for users.
- **Admin Interface**: Manage tasks through an intuitive admin interface.
- **API Endpoints**: Access endpoints to interact with tasks programmatically.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/task-management-app.git
   cd task-management-app

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

# Task_Managment
The Task Management Application, built with Python and Django, helps teams and individuals manage tasks efficiently. It supports task creation, updates, deadlines, user assignments, and completion status. Utilizing PostgreSQL for data storage and Docker for deployment, it ensures a reliable user experience.

