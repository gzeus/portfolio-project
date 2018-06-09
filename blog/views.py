from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def allblogs(request):
    blogs = Blog.objects.all()
    return render(request, "blog/allblogs.html", {"blogs":blogs})

def post(request, blog_id):
    post = get_object_or_404(Blog, pk=blog_id)
    return render(request, "blog/post.html", {"post":post})