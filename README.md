# Food Lovers API (Django REST Framework)

This API is developed for the Food Lovers React app and is powered by Django REST Framework. 
The Link to the deployed API can be found here: https://food-lovers.herokuapp.com/

The Link to the React app resository can be found here: https://github.com/KarlPreisler/foodlovers

---   [INSERT ERD]   ----

## Languages used

- [Python](https://www.python.org/)

## Workspace

### Gitpod
[GitPod](https://gitpod.io/)
- GitPod was used as the main IDE workspace to build this API.

## Version Control

### Git
[Git](https://git-scm.com/)
- Git was used as a version control system that allowed me to keep track of changes in my code over time.

### GitHub
[GitHub](https://github.com/) 
- GitHub stores the code for this project after being pushed from Git.

## Development

### Django Rest Framework
- [Django REST Framework](https://www.django-rest-framework.org/)
used to build the backend API.

### Django AllAuth
- [Django AllAuth](https://django-allauth.readthedocs.io/en/latest/index.html)
used for authentication of users.

## Hosting/Database

### Heroku
- [Heroku](https://id.heroku.com/login)
is used to host the application.

### Gunicorn
- [Gunicorn](https://gunicorn.org/)
used for deploying the application to Heroku.

### Cloudinary
- [Cloudinary](https://cloudinary.com/)
is used to store and host the media files.

### Pillow 
- [Pillow](https://pillow.readthedocs.io/en/stable/)
is used for image processing and validation.

### Psycopg2
- [psycopg2](https://www.psycopg.org/docs/)
is used for PostgreSQL Python adaption.

### PostgreSQL
- [PostgreSQL](https://www.postgresql.org/)
is used for the production database.

### PyJWT
- [PyJWT](https://pyjwt.readthedocs.io/en/stable/)
PyJWT for encode and decode JSON Web Tokens.

## Testing

### Manual testing:
- I have tested that the authentication and authorization functionality works as intended.
  - Signed in users can create a recipe.
  - Signed out users cant create a recipe.
  - Signed in users can like a recipe.
  - Signed out users can't like a recipe.
  - Signed in users can comment on a recipe.
  - Signed out users can't comment on a recipe.
- Profiles, comments, likes and recipes have Full CRUD Functionality through the API.  
- I have confirmed that the react app sends correct data to the API when creating, updating or deleting content.
- I have confirmed that API requests from the frontend are handled as intended on the backend. Updating, deleting och creating data is transmitted approprietly between the frontend and backend.

### Pep8
- PEP8 shows no errors for the project.

## Bugs
- There are no unfixed bugs.

## Deployment

This project is run using [Heroku](https://www.heroku.com), a cloud based platform that enables developers to build and run applications.
Here is the [Heroku documentation](https://devcenter.heroku.com/articles/heroku-cli) for the most recent installation instructions. 

### Local Deployment

To preview the project in the development environment, run the following command in the terminal:
```python3 manage.py runserver```. This will open port 8000. Click *Open Browser* when the popup window appears.

### ElephantSQL Deployment
I have used ElephantSQL to host my database. 
The instructions to create a new account can be[found here](https://code-institute-students.github.io/deployment-docs/02-elephantsql/elephantsql-01-sign-up). 
Once you have created an account:
- Log in to ElephantSQL.
- Click Create New Instance.
- Give your plan a name (usually the name of the project).
- Select the Tiny Turtle (Free) plan.
- Leave the Tags field blank.
- Click Select Region and choose a data center near you.
- Click Review and create an instance if everything looks correct.
- Go back to your dashboard and click on the name of the project. 
- Copy the database URL for your project.
- In your env.py file, create a new key called DATABASE_URL and give it the value of the ElephantSQL database URL, as follows: os.environ.setdefault("DATABASE_URL", "my_copied_database_url").
- Before deploying the project, if you dont already have one, create a file called env.py.
      - In settings.py: At the top of the file, add the following import:
      ```python
      import os
      if os.path.isfile("env.py"):
          import env
      ```
- Replace the pasted-in database url with the following code:
      ```python
      os.environ.get("DATABASE_URL")
      ```
- Add the database URL that was copied earlier and add it to the Config Vars in the Heroku settings

## Heroku deployment

1.  Clone this repository().
2.  In your IDE, connect to your repository, then enter this command in the terminal:
        
        pip install -r requirements.txt

3. Make sure your INSTALLED_APPS in settings.py matches the ones in this project.

3. Enter the following commands in the terminal:

        python manage.py makemigrations
        python manage.py migrate

4.  Git add, commit and push all changes to your repository.
5.  Create or log in to an account on Heroku.
6.  Create a new app on Heroku.
7.  Open your app on Heroku, go to Resources, Add-ons and search for PostgreSQL, then add it.
8.  In the Deploy tab on Heroku, go to deployment method and add your GitHub repository.
9.  In the Deploy tab on Heroku, go to manual deploy and select deploy branch.
10. Create or log in to an account on Cloudinary.
11. Copy your API Environment Variable.
12. Go back to Heroku, Settings and click on Reveal Config Vars.
13. Add these variables to your config vars. PostgreSQL DATABASE_URL should already be there.
    - ALLOWED_HOST | your_deployed_api_url
    - CLIENT_ORIGIN | your_deployed_frontend_url
    - CLIENT_ORIGIN_DEV | your_local_server_url
    - CLOUDINARY_URL | your_api_variable
    - SECRET_KEY | your_choice 
    - DISABLE_COLLECTSTATIC | 1
14. Create an env.py in the root directory, add it to .gitignore and add these lines at the top

        import os

        os.environ["SECRET_KEY"] = "your secret_key here"
        os.environ["CLOUDINARY_URL"] = "cloudinary url here"
        os.environ['DEV'] = '1'

15. In settings.py, update the CORS_ALLOWED_ORIGIN_REGEXES variable to match your local server url.

        if 'CLIENT_ORIGIN_DEV' in os.environ:
            extracted_url = re.match(r'^.+-', os.environ.get('CLIENT_ORIGIN_DEV', ''), re.IGNORECASE).group(0)
            CORS_ALLOWED_ORIGIN_REGEXES = [
                rf"{extracted_url}(eu|us)\d+\w\.gitpod\.io$",
            ]

16. Create a superuser for your site:

        python manage.py createsuperuser

17. To run your app locally, enter this command in your terminal:
        python manage.py runserver
        
## Acknowledgements
- Special thanks to my mentor Spencer for guidance throughout the project. With everything from styling and layout, to the functionality and logic of the project.
