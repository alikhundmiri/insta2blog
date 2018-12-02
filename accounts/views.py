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

import requests
import facebook
from facebook import GraphAPI


#  I M P O R T A N T
# app_id and app_secret must be variables from env... its not save to have them hardcoded here.	
app_id = '510918386043485'
app_secret = 'daacd3c037a86877e7566fc22165f3ba'


REDIRECT_BASE = 'http://localhost:8000/account/'
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
			return HttpResponseRedirect(reverse('blog:index'))
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

# STEP 1
def register_view(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse('blog:index'))
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

'''
 F A C E B O O K    A P P    P L A N

1. click on Register, SIGN UP ON WEBSITE
2. take user to Connect With Facebook (CWF)
3. ON CWF, click button
	take user to facebook_01():
		simple button which reditect to facebook login.
		GraphAPI().get_auth_url
	redirect to facebook_02():
		Show all Facebook Pages
3. Allow user to select a facebook page.
	Get the connected_instagram_account id
4. using Instagram ID, fetch past 10 posts, and make them to blog


PAGE 1
		register_view()
		Register on Insta2Blog

PAGE 2
		facebook_login()
		Register via facebook,
		
		OPENS NEW TAB, AUTHORISE VIA FACEBOOK

PAGE 3
		From Code/token, get the access_token
		ask user to pleaase wait. this will auto redirect to another page soon.

PAGE 4
		TBD facebook_pages()
		List of all Pages.
		Click on one Page Link, to connect via Facebook.

PAGE 5
		profile()
		Profile Page
'''
# ALTERNATIVE - STEP 2
@login_required
def facebook_login(request):
	# detect if user is logged in or not
	
	context = {
		'top_text' : 'Login to facebook',
		'form_text' : 'For accessing to instagram account, we need to login via your facebook, if you are already logged in, click "Continue"',
		'production' : settings.PRODUCTION,
		'tab_text' : 'Submit',

	}
	return render(request, 'accounts/facebook_login.html', context)

# STEP 2
@login_required
def facebook_login_view(request):
	# Check is user is online, connected to facebook.
	# if facebook is connected, send to facebook_login_view.
	# else, show facebook_login

	# This will get the link to login to the facebook app.
	facebook_login_url = get_user_access_token()
	context = {
		'top_text' : 'Login to facebook',
		'form_text' : 'For accessing to instagram account, we need to login via your facebook, if you are already logged in, click "Continue"',
		'production' : settings.PRODUCTION,
		'tab_text' : 'Continue With Facebook',
		'facebook_login_url' : facebook_login_url,

	}
	return render(request, 'accounts/facebook_login_view.html', context)

# After this the user will be redirected to a page where he will just wait and see a few redirects.


# STEP 3
@login_required
def facebook_get_code(request):
	#  This is a part of a series of redirects.


	"""
	This page will return either 'code' or 'token'


	1.	When 'code' is received, it has to be exchanged for an access token using an endpoint. The call will need to be server-to-server, since it involves your app secret. (Your app secret should never end up in client code.)
	2.	When 'token' is received, it needs to be verified. You should make an API call to an inspection endpoint that will indicate who the token was generated for and by which app. As this API call requires using an app access token, never make this call from a client. Instead make this call from a server where you can securely store your app secret.
	3.	When 'code' and 'token' are both received, both steps should be performed.
	
	Exchanging Code for an Access Token
	use GraphAPI().get_access_token_from_code()

	"""
	get_code = request.GET.get('code', '')
	get_token = request.GET.get('token', '')
	
	if get_code:
		access_token_ = get_access_token_code(get_code, 'facebook_pages')

	context = {
		'top_text' : 'Please wait',
		'form_text' : 'We are working on it',
		'production' : settings.PRODUCTION,

	}
	return render(request, 'accounts/facebook_pages.html', context)



# STEP 4
@login_required
def facebook_pages(request):
	context = {
		'top_text' : 'Select Facebook Page',
		'form_text' : 'Please Select the facebook Page which is connected to the Instagram Account you wish to Use.',
		'production' : settings.PRODUCTION,

	}
	return render(request, 'accounts/facebook_pages.html', context)

@login_required
def profile(request):
	context = {

		'production' : settings.PRODUCTION,	
	}
	return render(request, 'accounts/profile.html', context)

@login_required
def settings_page(request):
	# fetch bio and profession
	# ?fetch username
	context = {

		'production' : settings.PRODUCTION,
	}
	return render(request, 'accounts/settings.html', context)

@login_required
def logout_view(request):
	logout(request)
	return redirect('/')



##########################
# H E L P E R    F U N C T I O N S

# Just testing stuff.
def facebook_sdk_testing():
	redirect_uri = REDIRECT_BASE
 # THIS IS IMPORTANT... DO NOT COMMIT WITH THIS app_secret HERE.
	code_parameter = "alala"

	graph = facebook.GraphAPI(access_token="your_token", version="3.1")
	# Get the message from a post.
	post = graph.get_object(id='post_id', fields='message')
	print(post['message'])

# could be useful. but i dont use it yet.
def start_facebook_login():
	graph = facebook.GraphAPI(access_token=app_id , version="3.1")
	return graph

# Returns a Facebook login URL used to request an access token and permissions.
def get_user_access_token():
	canvas_url = REDIRECT_BASE + "facebook_get_code/"
	perms = ["manage_pages","instagram_basics"]
	fb_login_url = GraphAPI().get_auth_url(app_id, canvas_url, perms)
	print(fb_login_url)
	return fb_login_url

# after login, we get a "code" or 'token'. this code will give us access_token
def get_access_token_code(code_parameter, url_):
	redirect_uri = REDIRECT_BASE + url_

	perms = ["manage_pages", "instagram_basics"]

	# GET USER-SPECIFIC ACCESS TOKEN
	user_access_token = GraphAPI().get_access_token_from_code(code=code_parameter, redirect_uri=redirect_uri, app_id=app_id, app_secret=app_secret)
	print(user_access_token)
	
	return user_access_token
