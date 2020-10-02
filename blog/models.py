from django.db import models

class MyBlog(models.Model):

    title = models.CharField(max_length = 200)
    date = models.DateField()
    # TextField: holds more info rather than the regular char title
    description = models.TextField(max_length = 250)
    
    def __str__(self):
        return self.title