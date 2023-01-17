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

## Rest API call Structure

The functioning API calls at this moment are the following (all calls except the register and login api calls must include Web token as "Token [token_str]" in header ):


```
    POST /users/login
    # request body: username, password
    #################################################################

    POST /users/register
    # request body: username, password, email, optional: first_name, last_name

    #################################################################

    # the following API calls are for retrieving and modifying authenticated user's profile data

    GET /users/profile # retrieve user profile data from web token in headers

    PUT /users/profile # edit user profile data (enter the desired fields to update in request body)

    DEL /users/profile # delete user profile data

    #################################################################

    # the following calls are for finding other users in the application

    GET /users/contacts/find-users?search=[field] # find other users using query params. The API is set to work for partial or completely matching usernames, names and email addresses of other users. returns an array of user instances

    GET /users/contacts/view-user/[username] # get other user's profile data, except passwords

    #################################################################

    # the following calls are to set or retrieve blacklist status. A pair of user who are blacklisted cannot send direct messages to each other

    GET /users/contacts/blacklist-user/[username] # get the blacklist status of the user with username specified in url parameter
    # it will return a json object with the values for message (for event handling), is_blacklisted (bool), is_blacklisted_by_user (only the user who blacklisted can remove the blacklisted status)

    POST /users/contacts/blacklist-user/[username] # blacklists another user. The data model defines user1 as the authenticated user, and user2 as the user in the username url param
    # we can only blacklist an user if it is not being done yet

    DEL /users/contacts/blacklist-user/[username] # removes blacklist status
    # we can only delete blacklist entries in the database if there is an existing entry for the user1 (authenticated user) and user2 (in url param) pair

    #################################################################

    # the following calls are for retrieving contact list, and adding and removing contacts

    GET /users/contacts/contact-book/ # get all the contacts for the authenticated user
    
    POST /users/contacts/contact-book/[username] # add contact specified in url parameter to contact book

    DEL /users/contacts/contact-book/[username] # deletes contact specified in url parameter to contact book
```


## How to build and deploy this project?

At this moment, the project can be deployed on the cloud, in theory. As I test it myself I will be adding the how-to guides here in this section. I could point to references or explain how to due to past experience with cloud platforms, but I want to test it ON THIS PROJECT first when I have time before posting my own guides.

<br>

### Run locally

For this you should have set up a mysql database already, I won't explain this, as there are multiple ways of doing it. If you are using a remote database, you may need to modify this a bit. I will be adding a remote database config functionality when I make the cloud deployment guides. For this guide use your computer terminal, it is proved to work for ubuntu's default terminal and may or may not work with the git bash. Results may vary on others, some commands may not work the same way on cmd or powershell for example, or non debian linux distros. For steps such as creating and activating the virtual environment, please research on your own how to do it with the terminal that is available to you.

<br>

1. Clone this project using the following git command. Go to the parent folder you want to set up this project in:

<br>

```
    cd path/to/parent/project/folder
    git clone git@github.com:TheAttentionSeeker5050/chat-app-django-server.git
```

<br>

2. Go to the project folder just cloned, create a virtual environment and activate it (for ubuntu linux or wsl)

```
    cd chat-app-django-server
    python3 -m venv env
    source env/bin/activate
```

<br>

3. Install dependencies from requirements.txt into the activated environment:

```
    pip install -r requirements.txt
```

<br>

4. Add environment variables. The template for the enviroment variables is in the file ./main/dot_env_template. Create a new .env file on ./main/main/.env, and it should look like this:

```
    SECRET_KEY = myserverencryptionsecretkey
    MYSQL_PASSWORD = mysecretmysqluserpassword
    MYSQL_USER = mysqlusername
```

<strong>Note:</strong> Notice that the environment variables values have no commas, they should not.

<br>

5. Make your first database migration:

```
    python3 main/manage.py makemigrations
    python3 main/manage.py migrate
```

<br>

6. Add a superuser to access the django admin interface, and follow the steps on the prompt:

```
    django-admin main/manage.py createsuperuser
```

<br>

7. Run locally, or make changes to the git repo if you want

```
    python3 main/manage.py runserver
```

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

There are multiple ways on how to do this, I have tried myself on other projects using cloudflare and server runtimes like apache or nginx, so I would suggest you check specifically the server infrastructure guides as this is a very versatile and personalized approach, and there is not a single way to do this. I only have made this once, with my own blog app, and with manual in hand at all times. I would not call myself an expert on vps'es, and the fact that my blog still runs surprises me a lot. Still it is something I want to get good at some time.


