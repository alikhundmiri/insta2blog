from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.conf import settings
from django.urls import reverse
from django.http import Http404
import requests
# Create your views here.
from .models import blog
from accounts.models import insta_account
def index(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse('newsletter:index'))
	else:
		# pass
		return HttpResponseRedirect(reverse('accounts:profile'))

	context = {
		'production' : settings.PRODUCTION,
	}
	return render(request, 'accounts/profile.html', context)


def blog_list(request, insta_username=None):
	check_account = insta_account.objects.get(insta_username=insta_username)
	if check_account:
		pass
	else:
		raise Http404
	# get the blog list
	# print(check_account.insta_id)
	blogs = blog.objects.filter(insta_id__insta_username=check_account.insta_username)

	# print(blogs)
	# for blog_ in blogs:
	# 	print(blog_)

	context = {
		'insta_username' : insta_username,
		'user'	: check_account,
		'blogs' : blogs,
		'production' : settings.PRODUCTION,
		
	}
	return render(request, 'blog/blog_list.html', context)



def blog_detail(request, insta_username=None, slug=None):
	# get the blog post
	blog_post = get_object_or_404(blog, insta_id__insta_username=insta_username, blog_slug=slug)
	# print(blog_post)
	context = {
		'insta_username' : insta_username,
		'blog' : blog_post,
		'production' : settings.PRODUCTION,
	}
	return render(request, 'blog/blog_detail.html', context)


def blog_latest(request, insta_username=None):
	check_account = insta_account.objects.get(insta_username=insta_username)
	if check_account:
		pass
	else:
		raise Http404
	# get the latest blog post for the given user.
	blog_post = get_object_or_404(blog, insta_id__insta_username=insta_username).order_by('-id')[0]
	context = {
		'insta_username' : insta_username,
		'production' : settings.PRODUCTION,
	}
	return render(request, 'blog/blog_detail.html', context)