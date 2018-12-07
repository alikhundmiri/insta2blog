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

from accounts.views import (login_view, logout_view, register_view)


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('welcome/', include('newsletter.urls', namespace='newsletter')),
    path('account/', include('accounts.urls', namespace='accounts')),
    

    path('privacy_policy', TemplateView.as_view(template_name='privacy_policy.html') , name='privacy_policy'),
    path('term_of_use', TemplateView.as_view(template_name='term_of_use.html') , name='term_of_use'),

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),

    path('', include('blog.urls', namespace='blog')),

]


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)