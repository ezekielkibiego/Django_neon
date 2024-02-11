# Running the Django Neon Project

This guide explains how to set up and run the Django Neon project, a to-do application built using Django and Neon's serverless PostgreSQL.

## Prerequisites

Before getting started, ensure you have the following installed:

- Python >= 3.9.2
- Django
- psycopg2
- Neon cloud account

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/ezekielkibiego/Django_neon.git
    cd django_neon
    ```

2. Create and activate a Python virtual environment:

    ```bash
    python -m venv env
    source env/bin/activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Configure Neon credentials:

    - Open `django_neon/settings.py`.
    - Update the `DATABASES` settings with your Neon PostgreSQL connection details.

        Example configuration:

        ```python
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'your_database_name',
                'USER': 'your_neon_username',
                'PASSWORD': 'your_neon_password',
                'HOST': 'your_neon_host',
                'PORT': '5432',
                'OPTIONS': {'sslmode': 'require'},
            }
        }
        ```

5. Migrate the database:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

## Running the Server

To start the Django development server, run:

```bash
python manage.py runserver

```

## Usage

1. Access the application in your web browser at [http://127.0.0.1:8000//list/](http://127.0.0.1:8000/list/).
2. You can add new tasks by entering the task details in the provided form and clicking the "Add Task" button.
3. To delete a task, click the delete button next to the task you want to remove.



## Contributing

If you'd like to contribute to this project, please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License.