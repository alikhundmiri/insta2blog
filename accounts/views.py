from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import PasswordChangeForm
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse, Http404

from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	update_session_auth_hash
)
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404

from .forms import UserLoginForm, UserRegisterForm, InstaIDForm
# from accounts.forms import ProfileForm, EditProfileForm
def login_view(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse('accounts:profile'))
	next = ""

	if request.GET:  
		next = request.GET['next']

	dbug = settings.DEBUG
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		login(request,user)
		if next == "":
			# return HttpResponseRedirect("/")
			return HttpResponseRedirect(reverse('accounts:profile'))
		else:
			return HttpResponseRedirect(next)

	context = {
		"name_nav" : 'login',
		"nbar" : "login",
		"form" : form,
		"dbug" : dbug,
		'top_text' : 'Login',
		'form_text' : 'details',
		'tab_text' : 'Submit',
		'page' : 'full-page',
		'production' : settings.PRODUCTION,

	}
	return render(request, 'accounts/login.html', context)

def register_view(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse('accounts:profile'))
	next = ""

	if request.GET:
		next = request.GET['next']

	dbug = settings.DEBUG
	form = UserRegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get("password")
		user.set_password(password)
		user.save()
		new_user = authenticate(username=user.username, password=password)

		login(request, new_user)
		# change redirect to edit bio page
		# return HttpResponseRedirect("/")
		return HttpResponseRedirect(reverse('accounts:facebook_login'))
	context = {
		"name_nav" : 'register',	
		"nbar" : "register",
		"form" : form,
		'dbug' : dbug,
		'top_text' : 'Register',
		'form_text' : 'details',
		'tab_text' : 'Submit',
		'page' : 'full-page',
		'production' : settings.PRODUCTION,

	}
	return render(request, 'accounts/login.html', context)

@login_required
def settings_page(request):
	# fetch bio and profession
	# ?fetch username
	context = {

		'production' : settings.PRODUCTION,
	}
	return render(request, 'accounts/settings.html', context)

@login_required
def facebook(request):
	next = ''
	if request.GET:  
		next = request.GET['next']

	form = InstaIDForm(request.POST or None)
	if form.is_valid():
		insta_id = form.cleaned_data.get("insta_id")
		instance = form.save(commit=False)
		instance.save()
		if next == "":
			return HttpResponseRedirect(reverse('accounts:profile'))
		else:
			return HttpResponseRedirect(next)


	context = {
		'form' : form,
		'top_text' : 'Login to facebook',
		'form_text' : 'For accessing to instagram account, we need to login via your facebook, if you are already logged in, click "Continue"',
		'production' : settings.PRODUCTION,
		'tab_text' : 'Submit',

	}
	return render(request, 'accounts/facebook_login.html', context)


def profile(request):
	context = {

		'production' : settings.PRODUCTION,	
	}
	return render(request, 'accounts/profile.html', context)
@login_required
def logout_view(request):
	logout(request)
	return redirect('/')
