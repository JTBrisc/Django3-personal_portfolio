from django.contrib import admin

# import the model (Project) from the models.py (.models)
from .models import Project

# means: I want to see this model (Project) inside of the admin page.
admin.site.register(Project)
