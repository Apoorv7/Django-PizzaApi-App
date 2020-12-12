# Django-PizzaApi-App

## Environment Setup

### 1. Global dependencies

* [Install Python](https://www.python.org/downloads/)
* [Install Visual Studio Code](https://code.visualstudio.com/)
* [Install Postgresql](https://www.postgresql.org/)
* [Install pgAdmin4](https://www.pgadmin.org/download/)


* After installing these you can download the zip file of the github link then extract it and open the folder in Visual Studio Code app. 

* Then open pgAdmin4 and create a database dpa.
* In visual studio you have to install the remaining dependencies which you can find in the requirements.txt file.
* To download the dependencies you can use this command :-
    ```
      pip install -r requirements.txt
    ```
### 2. Setting up superuser for admin page and migrating models to database

* Also please change the postgres password in the settings.py file in dpa folder as per your given password or it will throw error.

* After setting global dependencies you need to migrate the models to the admin and the PostgreSql database.
    ```
        python manage.py makemigrations
    ```
    ```
        python manage.py migrate
    ```
    
* For creating a superuser you need to run this command :-
    ```
        python manage.py createsuperuser
    ```

 
## Running Server

* To start the server you need to enter this command :-
    ```
        python manage.py runserver
    ```
## Api links to Retrieve, Delete, Add and Alter data to database

* For Retriving all data :- ( Note : The port number can vary depending on your localhost )
    ```
    http://localhost:8000/api/pizzalist/
    ```
    
* For Adding data :- 
    ```
    http://localhost:8000/api/pizadd/
    ```
    
* For Alter/Delete data :- ( Note : Here 'i' is the id of the database you want to delete or alter which you can view from the retriving link )
    ```
    http://localhost:8000/api/pizalter/i/
    ```

