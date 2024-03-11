# joinup

## Setup and development

1. Install dependencies
```
poetry install
```

2. Apply migrations before running the project for the first time
```
poetry run python manage.py migrate
```

3. Start the web server (default localhost:8000)
```
poetry run python manage.py runserver
```

4. Start celery. IMPORTANT!! This requires __redis__ to run
```
poetry run celery -A core worker
```

5. Run the tests
```
poetry run python manage.py test
```

## Curl examples

### v1.0.0 signup
```
curl --location 'http://localhost:8000/api/v100/user/signup/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "Karelle90@hotmail.com",
    "first_name": "Bradley",
    "last_name": "Sanford",
    "phone": "+34642424242",
    "hobbies": "Quia facere quo iure eum tempora tempore earum excepturi."
}'
```

### v1.0.0 profile
```
curl --location 'http://localhost:8000/api/v100/user/1/profile/'
```

### v1.1.0 signup
```
curl --location 'http://localhost:8000/api/v110/user/signup/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "Jana2@gmail.com",
    "first_name": "Bernardo",
    "last_name": "Bergnaum",
    "phone": "+34642424242",
    "hobbies": "Saepe laudantium voluptas sequi qui iure autem possimus sint."
}'
```

### v1.1.0 profile
```
curl --location 'http://localhost:8000/api/v110/user/2/profile/'
```
