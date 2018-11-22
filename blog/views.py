from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, HttpResponseRedirect
from django.conf import settings
from django.urls import reverse
# Create your views here.

def index(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse('newsletter:index'))
		pass
	context = {
		'production' : settings.PRODUCTION,

	}
	return render(request, 'blog/blog_list.html', context)


def blog_list(request, username=None):
	context = {
		'production' : settings.PRODUCTION,
		'requested_user' : username,
	}
	return render(request, 'blog/blog_list.html', context)


def blog_latest(request, username=None):
	# if not request.user.is_authenticated:
	# 	return HttpResponseRedirect(reverse('newsletter:index'))
	context = {
		'production' : settings.PRODUCTION,
		'requested_user' : username,
	}
	return render(request, 'blog/blog_detail.html', context)


def blog_detail(request, username=None):
	context = {
		'production' : settings.PRODUCTION,
		'requested_user' : username,
	}
	return render(request, 'blog/blog_detail.html', context)

