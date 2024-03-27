from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from blog_register.forms import BlogForm  # Import for user authentication
from .models import Blog


def blog_list(request):
   
    query = request.GET.get('q')  # Get the search query from the request
    blogs = Blog.objects.all()
    if query:
        # Filter blog entries by title containing the search query
        blogs = blogs.filter(blog_title__icontains=query)
    return render(request, 'blog_register/blog_list.html', {'blog_list': blogs, 'query': query})
    

    

@login_required
def blog_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = BlogForm()
        else:
            blog = Blog.objects.get(pk=id)
            form = BlogForm(instance=blog)
        return render(request, "blog_register/blog_form.html", {'form': form})
    else:
        if id == 0:
            form = BlogForm(request.POST)
        else:
            blog = Blog.objects.get(pk=id)
            form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            # Set the author_name field of the form to the current user
            form.instance.author_name = request.user
            form.save()
            return redirect('/blog/list')
    return render(request, "blog_register/blog_form.html", {'form': form})

@login_required
def blog_delete(request,id):
    employee = Blog.objects.get(pk=id)
    employee.delete()
    return redirect('/blog/list')
