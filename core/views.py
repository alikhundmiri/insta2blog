from django.shortcuts import render, get_object_or_404
from django.http import (
	Http404, HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect,
)
from django.urls import reverse
# from newsletter.forms import NewsletterForm

# LANDING PAGE
def index(request):
	context = {
		'show_last_div' : False,
	}

	return render(request, 'landing.html', context)

def collect_email(request, variable):

	print(variable)
	context = {
		'show_last_div' : False,
	}
	return render(request, 'collect_email.html', context)


def paywall_test(request):
	context = {
		'show_last_div' : False,
	}
	return render(request, 'paywall_test.html', context)