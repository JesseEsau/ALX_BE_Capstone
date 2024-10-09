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

- Python 3.x
- Django 3.x or later
- Django REST Framework
- PostgreSQL (or any other database of your choice)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/event-management-api.git
   cd event-management-api
2. Create and activate virtual environment:
    python -m venv venv
    source venv/bin/activate  
3. Install dependencies:
    pip install -r requirements.txt
4. Setup environmental variables: Create a .env file and add your databse credentials, secret key, and other configurations.
5. Run migrations:
    python manage.py migrate
6. Create a superuser:
    python manage.py runserver

