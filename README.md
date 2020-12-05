# Django demo project

The project integrate 3 task

- django managament command to import customer.csv
- Rest API
- - Get: listing all customers
- - Post: getting one custumer by id
- Webapp
- - A simple webapp was created to consume this ResAPI

## Features:

- Database : sqllite3
- API services: Google Places API
- Project:<br>
  app1: apiapp<br>
  app2: webapp

## **Instalation:**

- Create your own python env
- Run the file requirements to download all the python libreries requiered to run this proyect.

        $pip install -r requirements.txt

- Make all migrations for run this proyects

        $python manage.py makemigrations
        $python manage.py migrate

## **Instructions:**

### Managament command **importcustomers**

1.  Management command to upload all the customers form a csv files, using well known fields. The command going to add to extra fields, latitude and longitud using [Places API ](https://developers.google.com/places/web-service/search#Fields) from google, specific [**Find places**](https://developers.google.com/places/web-service/search#FindPlaceRequests) end point.

        $python manage.py importcustomers path_file.csv

### REST API

### Webapp
