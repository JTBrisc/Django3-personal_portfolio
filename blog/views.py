from django.shortcuts import render, get_object_or_404
from .models import MyBlog

def all_blogs(request):
    # Grab the elements out of the DB
    blog = MyBlog.objects.all()

    # '-date' : the most current ones are going to pop on top
    # blog = MyBlog.objects.order_by('-date')

    # '-date' => the most current ones are going to pop on top
    # [:5]    => this is regular Python, going through a list, indicating 
    # the 1st 5 positions (i.e. posts)
    # blog = MyBlog.objects.order_by('-date')[:5]

    # Most recent 
    return render(request, 'blog/all_blogs.html', {'myBlog':blog})    

# passing to function 'detail' also the variable 'blog_id' created in urls.py
# (i.e. path('<int:blog_id>/',.....)
def detail(request, blog_id):
    post = get_object_or_404(MyBlog, pk=blog_id)
    return render (request, 'blog/detail.html', {'blog_post': post})
