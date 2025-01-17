# Variables
PROJECT_NAME = django-todo
DOCKER_COMPOSE = docker-compose
PYTHON = poetry run python

# ANSI color codes
RED = \033[0;31m
GREEN = \033[0;32m
YELLOW = \033[1;33m
BLUE = \033[0;34m
MAGENTA = \033[0;35m
CYAN = \033[0;36m
RESET = \033[0m

# Default target
.DEFAULT_GOAL := help

# Help target
help:
		@printf "$(CYAN)Available commands:$(RESET)\n"
		@printf "  $(GREEN)make build$(RESET)           Build the Docker containers\n"
		@printf "  $(GREEN)make up$(RESET)              Start the Docker containers\n"
		@printf "  $(GREEN)make down$(RESET)            Stop the Docker containers\n"
		@printf "  $(GREEN)make shell$(RESET)           Open a shell in the Django container\n"
		@printf "  $(GREEN)make migrate$(RESET)         Run Django migrations\n"
		@printf "  $(GREEN)make superuser$(RESET)       Create a Django superuser\n"
		@printf "  $(GREEN)make test$(RESET)            Run tests\n"
		@printf "  $(GREEN)make runserver$(RESET)       Run the Django development server\n"
		@printf "  $(GREEN)make poetry-install$(RESET)  Install Django dependencies with poetry\n"
		@printf "  $(GREEN)make poetry-add$(RESET)      Install new python dependency with poetry"

# Build Docker containers
build:
		@printf "$(YELLOW)Building Docker containers...$(RESET)\n"
		$(DOCKER_COMPOSE) build

# Start Docker containers
up:
		@printf "$(YELLOW)Starting Docker containers...$(RESET)\n"
		$(DOCKER_COMPOSE) up -d

# Stop Docker containers
down:
		@printf "$(YELLOW)Stopping Docker containers...$(RESET)\n"
		$(DOCKER_COMPOSE) down

# Open a shell in the Django container
shell:
		@printf "$(YELLOW)Opening a shell in the Django container...$(RESET)\n"
		$(DOCKER_COMPOSE) exec todo_api $(PYTHON) manage.py shell

# Run Django migrations
migrate:
		@printf "$(YELLOW)Running Django migrations...$(RESET)\n"
		$(DOCKER_COMPOSE) exec todo_api $(PYTHON) manage.py migrate

# Create a Django superuser
superuser:
		@printf "$(YELLOW)Creating a Django superuser...$(RESET)\n"
		$(DOCKER_COMPOSE) exec todo_api $(PYTHON) manage.py createsuperuser

# Run tests
test:
		@printf "$(YELLOW)Running tests...$(RESET)\n"
		$(DOCKER_COMPOSE) exec todo_api $(PYTHON) manage.py test

# Run the Django development server
runserver:
		@printf "$(YELLOW)Running the Django development server...$(RESET)\n"
		$(DOCKER_COMPOSE) exec todo_api $(PYTHON) manage.py runserver 0.0.0.0:8000

# Install Django dependencies with poetry in the container
# Run poetry lock and install dependencies
# add --no-dev to install only production dependencies
poetry-install:
		@printf "$(YELLOW)Installing Django dependencies...$(RESET)\n"
		$(DOCKER_COMPOSE) exec todo_api poetry lock
		$(DOCKER_COMPOSE) exec todo_api poetry install --no-root

# Install new python dependency with poetry
# add --dev to install only development dependencies
poetry-add:
		@printf "$(YELLOW)Adding new Python dependency...$(RESET)\n"
		$(DOCKER_COMPOSE) exec todo_api poetry add $(package)