from django.shortcuts import render
from .models import Post
from .forms import CreatePost
# Create your views here.

def dynamic_post_view (request, id):
    post = Post.objects.get(id=id)
    context = {"post": post}
    return render(request, "post.html", context)

def post_create(request):
    if request.method == "POST":
        form = CreatePost(request.POST)
        if form.is_valid():
            print("Posted")
            form.save()
    else:
        form = CreatePost()
        print("Not POsted")
    context = {'form': form}
    return render(request, 'createpost.html', context)
