# DWA_squarenet
SQUARENET - social network type web-app 

## Intro
backend --> Flask, ponyORM

set variables : 

**set FLASK_APP=app.py \
set FLASK_DEBUG=1** (only for debug)


## API URLs
### USERS
**Structure**

* id
* name
* email
* password

Users CRUD operations:

[POST, GET, PUT] /user

[DELETE] /user/{id_user}

Password update:

[PUT] /user/pass

Check login:

[GET]/user/{email}/{password}

### PROFILE
**Structure**

* id
* user
* gender
* age
* description
* tags

Profile CRUD operations:

[POST, PUT, GET] /profile

[DELETE] /profile/{profile_id}

Get profile per specific user:

[GET] /user/profile/{user_id}

### POSTS
**Structure**

* id
* title
* body
* time_posted
* user
* need_users
* due_time
* location
* apply_users
* tags

Posts CRUD operations:

[POST, PUT, GET] /posts

[DELETE] /posts/{post_id}

Get posts specific for user:

[GET] /homepage/{user_id}

Get posts of one user:

[GET] /profile_posts/{user_id}

### LOGINS
**Structure**

* id
* time
* first_login
* user

Update and read login:

[GET, POST]/login

### NOTIFICATIONS
**Structure**

* id
* time_created
* notification_type
* from_user
* to_user
* posts

Notifications CRUD operations:

[POST, PUT, GET] /notification

[DELETE] /notification/{notification_id}

Notifications for specific user:

[GET] /notification/user/{user_id}


### TAGS
**Structure**

* id
* name
* number_users

Get tags:

[GET]/tags
