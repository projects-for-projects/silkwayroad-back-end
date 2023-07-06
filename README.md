# silkwayroad-back-end

Django Rest Framework API server for Silkwayroad B2B project

## Technologies used
* [Django](https://www.djangoproject.com/): The web framework for perfectionists with deadlines (Django builds better web apps with less code).
* [DRF](www.django-rest-framework.org/): A powerful and flexible toolkit for building Web APIs


## Installation
* If you wish to run your own build, first ensure you have python globally installed in your computer. If not, you can get python [here](https://www.python.org").
* After doing this, confirm that you have installed virtualenv globally as well. If not, run this:
    ```bash
        $ pip install virtualenv
    ```
* Then, Git clone this repo to your PC
    ```bash
        $ git clone https://github.com/projects-for-projects/silkwayroad-back-end/
    ```

* #### Dependencies
    1. Cd into your the cloned repo as such:
        ```bash
            $ cd silkwayroad-back-end
        ```
    2. Create and fire up your virtual environment:
        ```Linux
            $ virtualenv venv -p python3
            $ source venv/bin/activate
        ```
        ```Windows
            $ python -m venv venv
            $ \venv\Scripts\activate
        ```
    3. Install the dependencies needed to run the app:
        ```bash
            $ pip install -r requirements.txt
        ```
    4. Make those migrations work
        ```bash
            $ python manage.py makemigrations
            $ python manage.py migrate
        ```

* #### Run It
    Fire up the server using this one simple command:
    ```bash
        $ python manage.py runserver
    ```
    You can now access the file api service on your browser by using
    ```
        http://localhost:8000/
    ```
