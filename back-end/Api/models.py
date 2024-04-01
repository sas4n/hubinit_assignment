from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class blog(models.Model):
    blog_title = models.CharField(max_length=50, blank=False)
    author_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogs")
    blog_text = models.TextField(blank=False)
    # The requirement here is A bit vague, as it wants the string only has two values (active and draft) which I nee to use
    # # choices but choices will result in a drop down which we are not allowed to have it. At the end I decided to use the
    # the normal charfield with a help text

    # ACTIVE = "ACTIVE"
    # DRAFT = "DRAFT"
    # # STATUS = {
    # #     ACTIVE: "Active",
    # #     DRAFT: "Draft",
    # # }
    # blog_status = models.CharField(max_length=6, choices=STATUS)
    blog_status = models.CharField(max_length=6, help_text= 'The value could be one of the following: Active or Draft')

    def __str__(self):
        return self.blog_title
