# Make workflow  

## Install require packages

```
pip install -r deploy/requirements.txt
```

## Testing 

After install requirements You should run tets.

```
cd base_app
pytest 
```

And also need check functional test

```
python manage.py test functional_tests.start
``


## For correct work socket need run redis in docker 

```
docker run -p 6379:6379 -d redis:5
```
