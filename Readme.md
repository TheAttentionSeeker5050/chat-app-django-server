# Chat server

<br>
<br>
<br>

<img src="https://images.pexels.com/photos/6636906/pexels-photo-6636906.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1">

<br>
<br>
<br>
<br>

A basic chat server application. At the moment is only text based, but will keep growing and adding some good features. It is still a work in progress. 

<br>
<br>
<br>

## Version 0.0.40

<br>
<br>

### Milestones

- Set the ground for the structure of the application. Almost all the models are created
- User app is almost completed, it is only lacking on permissions middleware based on blacklisted users (blacklist functionality was created as well)
- Configured django rest api, token web key is needed on all the rest api request to the server, except on login and register of course
- environment variables to hide sensitive passwords and string data
- Mysql server configured

<br>

### Technologies used

- Mysql database
- Django
- Django rest framework
- Token authentication
- Cors, although is disabled for local server run
- The app will have configuration entries stored in the server for stuff such as client theme and active hours, but not yet implemented. They will allow the client store them locally using technologies such as react redux

<br>
<br>
<br>

## How to build and deploy this project?

At this moment, the project can be deployed on the cloud, in theory. As I test it myself I will be adding the how-to guides here in this section. I could point to references or explain how to due to past experience with cloud platforms, but I want to test it ON THIS PROJECT first when I have time.

<br>

### Run locally

For this you should have set up a mysql database already, I won't explain this, as there are multiple ways of doing it. If you are using a remote database, you may need to modify this a bit. I will be adding a remote database config functionality when I make the cloud deployment guides. 

<br>

1. Clone this project using the following git command. Go to the parent folder you want to set up this project in:

<br>

<code>
    <p>cd path/to/parent/project/folder</p>
    <p>git clone git@github.com:TheAttentionSeeker5050/chat-app-django-server.git</p>
</code>

<br>

2. Go to the project folder just cloned, create a virtual environment and activate it (for ubuntu linux or wsl)

<code>
    <p>cd chat-app-django-server</p>
    <p>python3 -m venv env</p>
    <p>source env/bin/activate</p>
</code>

<br>

3. Install dependencies from requirements.txt into the activated environment:

<code>
    <p>pip install -r requirements.txt</p>
</code>

<br>

4. Add environment variables. The template for the enviroment variables is in the file ./main/dot_env_template. Create a new .env file on ./main/main/.env, and it should look like this:

<code>
    <p>
    SECRET_KEY = myserverencryptionsecretkey
    </p>
    <p>
    MYSQL_PASSWORD = mysecretmysqluserpassword
    </p>
    <p>
    MYSQL_USER = mysqlusername
    </p>
</code>

<strong>Note:</strong> Notice that the environment variables values have no commas, they should not.

<br>

5. Make your first database migration:

<code>
    <p>python3 main/manage.py makemigrations</p>
    <p>python3 main/manage.py migrate</p>
</code>

<br>

6. Add a superuser to access the django admin interface, and follow the steps on the prompt:

<code>
    <p>django-admin main/manage.py createsuperuser</p>
</code>

<br>

7. Run locally, or make changes to the git repo if you want

<code>
    <p>python3 main/manage.py runserver</p>
</code>

<br>

### Deploy on heroku

Work in progress. For more info try the following link:
https://devcenter.heroku.com/articles/django-app-configuration

<br>

### Deploy on google cloud
Work in progress. For more info try the following link:
https://cloud.google.com/python/django

<br>

### Deploy on AWS


Work in progress. For more info try the following link:
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html

<br>

### Deploy on other platforms manually on VPS

There are multiple ways on how to do this, I have tried myself on other projects using cloudflare and server runtimes like apache or nginx, so I would suggest you check specifically the server infrastructure guides as this is a very versatile and personalized approach, and there is no a single way to do this. I only have made this once, with my own blog app, and with manual in hand at all time. I would not call myself an expert on vps'es, and the fact that my blog still runs surprises me a lot. Still it is something I want to get good at some time.


