from django.contrib import admin

# import the model (MyBlog) from the models.py (.models)
from . models import MyBlog

# means: I want to see this model (MyBlog) inside of the admin page.
admin.site.register(MyBlog)

