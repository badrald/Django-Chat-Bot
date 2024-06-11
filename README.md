# Chatbot Project

This project is a web-based chatbot application developed using the Grom framework, Django for the back-end, and Bootstrap for the front-end.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- Interactive chatbot interface
- Responsive design using Bootstrap
- Backend powered by Django
- Easily extensible and customizable

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8+
- Node.js and npm (for Grom)
- Django 3.0+
- Bootstrap 4 or 5

## Installation

### Backend (Django)

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/chatbot-project.git
    cd chatbot-project
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Run database migrations:
    ```sh
    python manage.py migrate
    ```

5. Create a superuser to access the Django admin:
    ```sh
    python manage.py createsuperuser
    ```

### Frontend (Grom and Bootstrap)

1. Navigate to the frontend directory:
    ```sh
    cd frontend
    ```

2. Install the necessary npm packages:
    ```sh
    npm install
    ```

3. Build the frontend assets:
    ```sh
    npm run build
    ```

## Running the Application

1. Start the Django development server:
    ```sh
    python manage.py runserver
    ```

2. Open your web browser and navigate to `http://localhost:8000` to see the chatbot in action.

## Project Structure

```plaintext
Django-Chat-Bot/
├── accounts/
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── views.py
├── Bot/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── chat/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── views.py
├── manage.py
└── requirements.txt
├── templates/
│   ├── accounts/
|   |  |-- login.html
|   |  |-- profile.html
│   ├── chat/
│   │   ├── index.html
│   ├── base.html
└── README.md
Usage
Access the Django admin interface at http://localhost:8000/admin to manage chatbot settings.
Chat with the bot on the main page and interact with its features.
Contributing
Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Make your changes.
Commit your changes (git commit -m 'Add your feature').
Push to the branch (git push origin feature/your-feature).
Open a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for more information.

Contact
badr alden abduall - badrgta51@gmail.com

Project Link: (https://github.com/badrald/Django-Chat-Bot)
