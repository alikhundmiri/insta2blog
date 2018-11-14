from django.shortcuts import render
from django.conf import settings
# Create your views here.
def index(request):
	context = {
		'show_last_div' : False,
		'production' : settings.PRODUCTION,
	}

	return render(request, 'testpage.html', context)

