from django.shortcuts import render, get_object_or_404
from django.http import (
	Http404, HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect,
)
from django.urls import reverse
from django.conf import settings

from newsletter.forms import NewsletterForm
from newsletter.models import newsletter_list
# LANDING PAGE
def index(request):
	if request.method == 'POST':
		form = NewsletterForm(request.POST or None)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.threshold = newsletter_list.THRESHOLD_LIST[0][0]
			instance.save()
			return HttpResponseRedirect(reverse('core:thankyou'))
	else:
		form = NewsletterForm()
	context = {
		'form' : form,
		'show_last_div' : False,
		'production' : settings.PRODUCTION,
	}

	return render(request, 'landing.html', context)

def thankyou(request):
	context = {
		'show_last_div' : False,
		'production' : settings.PRODUCTION,
	}

	return render(request, 'thankyou.html', context)

def features(request):
	
	if request.method == 'POST':
		form = NewsletterForm(request.POST or None)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.threshold = newsletter_list.THRESHOLD_LIST[0][0]
			instance.save()
			return HttpResponseRedirect(reverse('core:thankyou'))
	else:
		form = NewsletterForm()
	context = {
		'form' : form,
		'show_last_div' : False,
		'production' : settings.PRODUCTION,
	}

	return render(request, 'features.html', context)

def newsletter_signup(request):
	if request.method == 'POST':
		form = NewsletterForm(request.POST or None)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.threshold = newsletter_list.THRESHOLD_LIST[0][0]
			instance.save()
			return HttpResponseRedirect(reverse('core:thankyou'))
	else:
		form = NewsletterForm()


	context = {
		'form' : form,
		'show_last_div' : False,
		'production' : settings.PRODUCTION,
	}
	return render(request, 'newsletter_signup.html', context)

def collect_email(request, variable=None):

	if request.method == 'POST':

		threshold_ = None
		if variable == 'one':
			threshold_ = newsletter_list.THRESHOLD_LIST[0][0]
		elif variable == 'two':
			threshold_ = newsletter_list.THRESHOLD_LIST[1][0]
		elif variable == 'three':
			threshold_ = newsletter_list.THRESHOLD_LIST[2][0]
		else:
			threshold_ = newsletter_list.THRESHOLD_LIST[0][0]

		form = NewsletterForm(request.POST or None)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.threshold = threshold_
			instance.save()
			return HttpResponseRedirect(reverse('core:thankyou'))
	else:
		form = NewsletterForm()


	context = {
		'form' : form,
		'show_last_div' : False,
		'production' : settings.PRODUCTION,
	}
	return render(request, 'collect_email.html', context)


def paywall_test(request):
	if request.method == 'POST':
		form = NewsletterForm(request.POST or None)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.threshold = newsletter_list.THRESHOLD_LIST[0][0]
			instance.save()
			return HttpResponseRedirect(reverse('core:thankyou'))
	else:
		form = NewsletterForm()
	context = {
		'form' : form,
		'show_last_div' : False,
		'production' : settings.PRODUCTION,
	}
	return render(request, 'paywall_test.html', context)