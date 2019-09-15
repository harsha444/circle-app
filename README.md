# BLOGS REST API
To run the app, use the following steps

`git clone https://github.com/harsha444/circle-app.git`


cd circle-app/

docker-compose build

### To run migrations
```
docker-compose run app python manage.py makemigrations
docker-compose run app python manage.py makemigrations users
docker-compose run app python manage.py makemigrations blog
docker-compose run app python manage.py migrate
docker-compose run app python manage.py migrate users
docker-compose run app python manage.py migrate blog
```

Note: If you get a `django.db.migrations.exceptions.NodeNotFoundError:` error while running migrations, please do the following and rerun the above commands Else proceed to Next step(generating fake data)
```
docker-compose run app rm -rf users/migrations
docker-compose run app rm -rf blog/migrations
```

### Generating Fake data
```
docker-compose run app python populate_data.py
```
(You'll be asked a set of questions, fill that and it might take some time for it to get populated)

### Run the server
```
sudo docker-compose run app
```
This will start server at 127.0.0.1 in your local machine.

Note: If the server doesn't start in your local machine, get the IP from the command
`sudo docker-compose run app sh -c ifconfig`
and add the *inet addr* given in *app/blog_project/settings.py* `ALLOWED_HOSTS` field and and run the server from above command.

Now the server will be live on either 127.0.0.1:8000 or the inet addr:8000 that we get from above.

# APIs
The project currently has APIs for
1) Creating a user, Updating a user, Deleting a user and applying a patch on user
Endpoint: `http://127.0.0.1:8000/api/users/profile/<user_profile_id>`
2) Getting a list of users
Endpoint: `http://127.0.0.1:8000/api/users/profile/>`

3) Creating a Blog, Updating a Blog, Deleting a Blog and applying a patch on Blog
Endpoint: `http://172.21.0.3:8000/api/blogs/blog/<blog_id>`
4) Getting list of all blogs
Endpoint: `http://172.21.0.3:8000/api/blogs/blog/`

5) Getting the common blogs of first level friends of users of a blog
`http://127.0.0.1:8000/api/blogs/common/<blog_id>/`