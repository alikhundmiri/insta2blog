"""insta2blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

from . import views

app_name = "blog"

urlpatterns = [
	path('', views.index , name='index'),
    path('<str:insta_username>/', include([

        path('', views.blog_list, name='blog_list'),
        path('new/', views.blog_latest, name='blog_latest'),
        path('<str:slug>/', views.blog_detail, name='blog_detail'),

    ])),

    # path('facebook/', views.facebook, name='facebook_login'),
    # path('profile/', views.profile, name='profile'),

]