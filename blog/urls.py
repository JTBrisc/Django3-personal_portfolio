from django.urls import path

# we are using the '.' because 'views' are inside the same folder
from . import views

app_name = 'blog'

urlpatterns = [
    # path to display all the blogs (this is the 'home' page of the blogs) !
    # In the same folder containing this file (urls.py) go to views.py 
    # (this is why is imported with '.'), and call function: 'all_blogs' 
    path('', views.all_blogs, name="all_blogs"),

    path('<int:blog_id>/', views.detail, name="detail"),
]
