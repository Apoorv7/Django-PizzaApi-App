# Django-PizzaApi-App

## Environment Setup

### 1. Global dependencies

* [Install Python](https://www.python.org/downloads/)
* [Install Visual Studio Code](https://code.visualstudio.com/)
* [Install Postgresql](https://www.postgresql.org/)
* [Install pgAdmin4](https://www.pgadmin.org/download/)

* After installing these you can download the zip file of the github link and open the folder in Visual Studio Code app.
* In visual studio you have to install the remaining dependencies which you can find in the requirements.txt file.
* To download the dependencies you can use this command :-
    ```
      pip install -r requirements.txt
    ```
### 2. Setting up superuser for admin page and migrating models to database

* For creating a superuser you need to run this command :-
    ```
        python manage.py createsuperuser
    ```
* After setting this up you need to migrate the models to the admin and the PostgreSql database.
    ```
        python manage.py makemigrations
    ```
    ```
        python manage.py migrate
    ```
 
## Running Server

* To start the server you need to enter this command :-
    ```
        python manage.py runserver
    ```
## Api links to Retrieve, Delete, Add and Alter data to database

* For Retriving all data :-
  Note that port number can vary depending on your localhost
    ```
    http://localhost:8000/api/pizzalist/
    ```
    
* For Adding data - http://localhost:8000/api/pizadd/
* For Alter/Delete data - http://localhost:8000/api/pizalter/i/ <!-- Note that here 'i' is the id of the database you want to delete or alter which you can view from the retriving link --->

