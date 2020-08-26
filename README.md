
# Codeleap backend test by Lucas Weber

### Description
This is an API for creating, editing and deleting Posts.

For demonstration purposes all user authentication and specific permissions verification has been disabled, so you can access all endpoints without login in.


### Dependencies
* python3.6
* asgiref==3.2.10
* dj-database-url==0.5.0
* Django==3.1
* django-heroku==0.3.1
* djangorestframework==3.11.1
* gunicorn==20.0.4
* psycopg2==2.8.5
* pytz==2020.1
* sqlparse==0.3.1
* whitenoise==5.2.0


### Services

* **GET https://codeleap.herokuapp.com/careers/** - Get a list of Posts

* **POST https://codeleap.herokuapp.com/careers/** - Add a new Post

    Body:

    {
        "title": "New Post",
        "username": "John Doe",
        "content": "New content for a post"
    }

* **PATCH https://codeleap.herokuapp.com/careers/{ID}/** - Update an existent Post by ID

    Body:

    {
        "title": "Edited Post",
        "content": "This content has been edited"
    }

* **DELETE https://codeleap.herokuapp.com/careers/{ID}/** - Delete an existent Post by ID


### Environment

This code was developed using Intel® Core™ i5-7300HQ CPU @ 2.50GHz × 4, 16GB RAM

OS: Linux - Ubuntu 18.04.3 LTS

All python libs were installed inside a virtualenv


#### If you have any problems or doubts executing this, please call me!

#### weberxw@gmail.com
