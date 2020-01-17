"""Demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
import Forum.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/<int:id>/', views.dynamic_post_view, name="post"),
    path('createpost', views.post_create, name="create"),
    path('feed', views.feed, name = "feed"),
    path('', views.feed, name = "index"),
    path('register', views.register, name = "register"),
    path('login', views.login, name = "login"),
    path('', include("django.contrib.auth.urls")),

]
