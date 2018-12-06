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

app_name = "accounts"

urlpatterns = [
    path('profile/', views.profile, name='profile'),

    path('facebook/', views.facebook_login, name='facebook_login'),
	path('facebook_pages/', views.facebook_pages, name='facebook_pages'),
	path('facebook_get_code/', views.facebook_get_code, name='facebook_get_code'),
	path('facebook_login_view/', views.facebook_login_view, name='facebook_login_view'),	
	path('insta_account_setup/<int:insta_id>', views.insta_account_setup, name='insta_account_setup'),
    

]