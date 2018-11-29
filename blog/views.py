from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, HttpResponseRedirect
from django.conf import settings
from django.urls import reverse

import requests
# Create your views here.


def index(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse('newsletter:index'))
	# else:
	# 	return HttpResponseRedirect(reverse('accounts:profile'))
		pass
	context = {
		'production' : settings.PRODUCTION,
		'requested_user' : request.user.username,
	}
	return render(request, 'blog/blog_list.html', context)


def blog_list(request, username=None):

	url = 'https://graph.facebook.com/v3.2/17841404624166068/media?access_token=EAAHQrXToyl0BAPW0vfxXYJ1CqdgcPI64RoZBH9A1MsMnBmmqCPd7fDIYWAOyeCtDd7LR6g8SXCWczeyZBg35Ed8ZB96gMsbd2drFOfl7PgJKCl8KUZBMEwwkvSniBPCGXFCDZBGpZBDpGdf7FtFiFYgE6FHR9mYVoZAMPZA6tkanfF0y05nCpXyz61RPxNGL5G8ZD&pretty=0&fields=caption&limit=2'
	req = requests.get(url)
	response = req.json()

	print(response)
	
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

