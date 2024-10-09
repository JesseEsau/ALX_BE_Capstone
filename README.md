# Event Management API
This project is a RESTful API for managing events, including features for user authentication, event creation, feedback on past events, tagging, and filtering of events. It allows users to register, create events, categorize them, leave feedback on events, and filter events based on tags or other criteria.

## Features

- User authentication and registration
- CRUD operations for events
- Event categorization
- Event search and filter
- User feedback and comments on past events
- Token-based authentication using JWT

## Project Setup

### Prerequisites

- Python==3.x
- Django==5.1.1
- djangorestframework==3.15.2
- djangorestframework-simplejwt==5.3.1
- drf-spectacular==0.27.2
- Django REST Framework
- django-filter==24.3
- django-taggit==6.1.0
- PostgreSQL (or any other database of your choice)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/event-management-api.git
   cd event-management-api
2. Create and activate virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
4. Setup environmental variables: Create a .env file and add your databse credentials, secret key, and other configurations.
5. Run migrations:
    ```bash
    python manage.py migrate
6. Create a superuser:
    ```bash
    python manage.py runserver

