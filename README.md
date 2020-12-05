# Django demo project

The project integrate 3 task

- django managament command to import customer.csv
- Rest API
- - Get: listing all customers
- - Post: getting one custumer by id
- Webapp
- - A simple webapp that consume this ResAPI, show documentation, builded with [django-yasg](https://github.com/axnsan12/drf-yasg)

<img src="imgs/yasg.PNG" alt="drawing" width="600"/>

### Compatible with

- Django Rest Framework 3.11 , 3.12
- Django 3.0 3.1
- Python 3.6 , 3.7
- googlemaps 4.4

### Resources:

- Live demo:
- source : https://github.com/DavidCastilloAlvarado/demo_django_API
- source googlemaps: https://github.com/googlemaps/google-maps-services-python
- documentation django: https://docs.djangoproject.com/en/3.1/
- documentation django-yasg: https://drf-yasg.readthedocs.io/en/stable/
- documentation googlemaps: https://developers.google.com/places/web-service/search#FindPlaceRequests

## Features:

- Database : sqllite3
- API services: Google Places API
- Project:<br>
  app1: apiapp<br>
  app2: webapp

## **Installation:**

1.  Clone this repo

        $git clone https://github.com/DavidCastilloAlvarado/demo_django_API

        $cd demo_django_API

2.  Install and active the enviorment (windows)

        $python -m pip install --user virtualenv
        $python -m venv .
        $.\Scripts\activate

3.  Download all libreries requierements

        $pip install -r requirements.txt

## **Quickstart**

1. Set your own setting.py file

In `settings.py`:

```python

   INSTALLED_APPS = [
      ...
      # Google APLI KEY
      GCP_API_KEY = 'AIzaSyDKpi89I2bMbJIBtxukASftmpMF6PwtLZg'
      # Dir templates, absolute path
      DIR_TEMPLATES = "I:/Documentos/Gdrive/django/demoeng/webapp/template"
      ...
   ]
```

2.  Make all migrations for run this proyects

        $python manage.py makemigrations
        $python manage.py migrate

3.  Run server

        $python manage.py runserver

## **Using**

1.  **Management command**: Upload all the customers fields from a csv files, our dbmodel already know this fields. The command going to add to extra fields, latitude and longitud using [Places API ](https://developers.google.com/places/web-service/search#Fields) from google, specific [**Find places**](https://developers.google.com/places/web-service/search#FindPlaceRequests) end point base on city field.

            $python manage.py importcustomers path_file.csv

    <center>
    <img src="imgs/customers.PNG" alt="drawing" width="700"/>
    </center>

### REST API / webapp

2.  Home page:
You can chose two view, swagger-ui or redoc
<center>
<img src="imgs/home.PNG" alt="drawing" width="1000"/>
</center>

3.  Swagger-ui: You can see two methods, get and post.

              Get method going to return the whole list of customer saved on our data base.

    <center>
    <img src="imgs/get.PNG" alt="drawing" width="1000"/>
    </center>

            Post method, made a reques using the parameter "id", then response (a single json) with the data of the customer with id == "id"

    <center>
    <img src="imgs/post.PNG" alt="drawing" width="1000"/>
    </center>
