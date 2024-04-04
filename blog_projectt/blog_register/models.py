from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    blog_title = models.CharField(max_length=50)
    author_name = models.ForeignKey(User, on_delete=models.CASCADE)  
    blog_text = models.TextField()
    blog_status = models.CharField(max_length=10)
    
    def __str__(self):
        return self.blog_title