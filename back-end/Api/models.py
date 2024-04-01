from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class blog(models.Model):
    blog_title = models.CharField(max_length=50)
    author_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogs")
    blog_text = models.TextField()
    ACTIVE = "ACTIVE"
    DRAFT = "DRAFT"
    STATUS = {
        ACTIVE: "Active",
        DRAFT: "Draft",
    }
    blog_status = models.CharField(max_length=6, choices=STATUS)

