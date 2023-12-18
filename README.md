json file upload endpoint is :      http://127.0.0.1:8000/upload/

we can use postman for testing file upload , 
key name should be "file" while using postman

Once, the file is uploaded data is serialized for every entry of the json and saved into the database



Docker:

- docker-compose up
- docker-compose build


Details:

I used django-rest-framework 
My database model is in api > models.py
My serializer is in api > serializers.py
the main framework functionality is in api > views.py
Urls are declared in api > urls.py 

Data can be retrieved from the database and aggregation can be applied to ensure that requirements are fulfilled.
