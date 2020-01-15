from django.shortcuts import render
from .models import Post

# Create your views here.

def dynamic_post_view (request, id):
    post = Post.objects.get(id=id)
    context = {
        "post": post
    }
    return render(request, "index.html", context)
