from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CreatePost
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
@login_required
def dynamic_post_view (request, id):
    post = Post.objects.get(id=id)
    context = {"post": post}
    return render(request, "post.html", context)

@login_required
def dynamic_account_view (request, username):
    account = User.objects.get(username=username)
    context = {"account": account}
    return render(request, "user.html", context)

@login_required
def post_create(request):
    if request.method == "POST":
        form = CreatePost(request.POST)
        print("Created")
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            form.save()
            return HttpResponseRedirect('/post/' + str(Post.objects.latest('id').id))
    else:
        form = CreatePost()
        print("Retrieved")
        context = {'form': form}
        return render(request, 'createpost.html', context)

@login_required
def feed(request):
    posts = Post.objects.order_by('id')
    context = {"posts": posts}
    return render(request, "feed.html", context)

def register(response):
    if response.method == "POST":
        form =  UserCreationForm(response.POST)
        print('Posted')
        if form.is_valid():
            form.save()
            print('Done')
            return HttpResponseRedirect('/login')
    else:
        form =  UserCreationForm()
        context = {'form':form}
        return render(response, "register.html", context)
