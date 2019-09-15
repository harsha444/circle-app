from faker import Faker
import os, sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'blog_project.settings'
ROOT_FOLDER = os.path.realpath(os.path.dirname(__file__))
splits = ROOT_FOLDER.split('/')

import django

django.setup()

import random
from users.models import UserProfile
from blog.models import Blog, UserBlogComment

fake = Faker()

n_blogs = int(input("How many blogs do you want to create? : "))
n_users = int(input("How many users do you want to create? : "))
n_comments_min_range = int(input("What is the minimum number of blogs a user can comment on? :"))
n_comments_max_range = int(input("What is the maximum number of blogs a user can comment on? :"))

# Creating Blogs

for _ in range(n_blogs):
    print("Seeding Blogs data")
    Blog.objects.create(
        heading=fake.catch_phrase(),
        text=fake.text()
    )

for _ in range(n_users):
    print("Seeding users and comments data")
    up = UserProfile.objects.create(phone=fake.phone_number(), name=fake.name())
    for i in range(random.randint(n_comments_min_range, n_comments_max_range)):
        try:
            blog_id = random.randint(0, n_blogs)
            UserBlogComment.objects.create(
                user=up,
                blog_id=blog_id,
                comment=fake.paragraph()
            )
        except:
            continue
