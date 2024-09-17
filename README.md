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
