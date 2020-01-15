from django.shortcuts import render, redirect
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
        print("Created")
        if form.is_valid():
            print("Posted")
            form.save()
            return redirect('post')
    else:
        form = CreatePost()
        print("Retrieved")
        context = {'form': form}
        return render(request, 'createpost.html', context)
