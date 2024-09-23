# Use official Python runtime as a parent image
FROM python:3.12-slim-bullseye

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

#  Copy the Poetry configuration files
COPY pyproject.toml poetry.lock /app/

# Install Poetry
RUN pip install poetry

# Install project dependencies
RUN poetry install --no-root

# Copy the project files
COPY . /app/

# Expose the port that Django will run on
EXPOSE 8000

# Define the command to run the Django development server
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
