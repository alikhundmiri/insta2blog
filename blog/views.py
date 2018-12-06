from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, HttpResponseRedirect
from django.conf import settings
from django.urls import reverse
from django.http import Http404
import requests
# Create your views here.
from .models import blog
# from accounts.models import insta_account
def index(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse('newsletter:index'))
	else:
		pass
		# return HttpResponseRedirect(reverse('accounts:profile'))

	context = {
		'production' : settings.PRODUCTION,
	}
	return render(request, 'accounts/profile.html', context)


def blog_list(request, insta_username=None):

	context = {
		'production' : settings.PRODUCTION,
		
	}
	return render(request, 'blog/blog_list.html', context)


def blog_latest(request):
	# if not request.user.is_authenticated:
	# 	return HttpResponseRedirect(reverse('newsletter:index'))
	context = {
		'production' : settings.PRODUCTION,
	}
	return render(request, 'blog/blog_detail.html', context)


def blog_detail(request, insta_username=None, slug=None):
	context = {
		'production' : settings.PRODUCTION,
	}
	return render(request, 'blog/blog_detail.html', context)

