from django.shortcuts import render, get_object_or_404
from django.http import (
	Http404, HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect,
)
from django.urls import reverse

from newsletter.forms import NewsletterForm
from newsletter.models import newsletter_list
# LANDING PAGE
def index(request):
	context = {
		'show_last_div' : False,
	}

	return render(request, 'landing.html', context)

def thankyou(request):
	context = {
		'show_last_div' : False,
	}

	return render(request, 'thankyou.html', context)

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
	}
	return render(request, 'collect_email.html', context)


def paywall_test(request):
	context = {
		'show_last_div' : False,
	}
	return render(request, 'paywall_test.html', context)