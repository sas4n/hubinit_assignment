from django import forms
from .models import Blog
from django.contrib.auth.models import User



class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ['blog_title', 'author_name', 'blog_text', 'blog_status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Retrieve all users from the User model
        users = User.objects.all()
        # Populate choices for the author_name field with user usernames
        self.fields['author_name'].queryset = users
        
