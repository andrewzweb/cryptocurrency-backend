# Make workflow  

## Install require packages

```
pip install -r deploy/requirements.txt
```

## Testing 

After install requirements you should run tets.

```
cd base_app
pytest
```

And also need check functional test

```
python manage.py test functional_tests.start
```


## For correct work socket need run redis in docker before start 

```sh
docker run -p 6379:6379 -d redis:5
```

## Run django(wsgi) and daphne(asgi)

Go to main folder base_app and run two command in different terminals

```sh
daphne base_app.asgi:application --bind 0.0.0.0 --port 8001
```

```sh
gunicorn -w 3 -b 0.0.0.0:8000 base_app.wsgi:application 

```
