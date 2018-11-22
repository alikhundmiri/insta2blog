from django.shortcuts import render, get_object_or_404
from django.http import (
	Http404, HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect,
)
from django.urls import reverse
from django.conf import settings

# LANDING PAGE
def new_blog(request):
	
	context = {
		'show_last_div' : False,
		'production' : settings.PRODUCTION,
	}

	return render(request, 'core/user_profile.html', context)
