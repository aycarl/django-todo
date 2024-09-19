# Django Todo App

A simple Django-based Todo application to manage your tasks efficiently.

## Description

This project is a basic Todo application built with Django. It allows users to create, read, update, and delete tasks. Each task has a title, content, and a completion status.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/django-todo.git
    cd django-todo
    ```

2. **Setting up a local custom domain**:

    Edit /etc/hosts File: Add an entry to your /etc/hosts file to map a custom domain to localhost.

    ```bash
    sudo nano /etc/hosts
    ```

    Add the following line to the file:

    ```text
    127.0.0.1       your-custom-domain.local   # e.g. aycarl.local
    127.0.0.1       todo-api.<your-custom-domain>.local   # e.g. todo-api.aycarl.local
    ```

    Save and close the file.

    Update docker-compose.yml: Update your docker-compose.yml to configure Traefik and your Django service for local development.

2. **Install Poetry**:
    Follow the instructions on the [Poetry website](https://python-poetry.org/docs/#installation) to install Poetry.

3. **Install dependencies**:
    ```bash
    poetry install
    ```

4. **Activate the virtual environment**:
    ```bash
    poetry shell
    ```

5. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

6. **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

## Usage

1. **Access the application**:
    Open your web browser and go to `http://127.0.0.1:8000`.

2. **Admin Panel**:
    Access the admin panel at `http://127.0.0.1:8000/admin` to manage tasks.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License.
