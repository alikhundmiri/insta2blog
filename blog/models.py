from django.db import models
from django.conf import settings


from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify


from accounts.models import insta_account


class blog(models.Model):
	# a paid user can have up to 5 instagram accounts connected. This is where we store insta bio, user, 
	# insta_id, 
	user 					=			models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	# each blog post belongs to a single insta_account. each insta2blog user can have max 5 insta_accounts 
	insta_id				=			models.ForeignKey(insta_account, on_delete=models.CASCADE)
	# save the caption, here
	blog_caption			=			models.TextField(max_length=2200, blank=True, null=True, default="user bio here")
	# after processing, save the title here
	blog_title				=			models.TextField(max_length=300)
	# and the post here
	blog_post				=			models.TextField(max_length=2200)
	# and here lies the slug. LOL.
	blog_slug				=			models.SlugField(max_length=255, unique=True)
	# fetch and save the link in bio here
	link_in_bio				=			models.URLField(max_length=1000, blank=True, null=True)
	

	# add a field to enable user's custom bio, or load directly from Instagram. A simple boolean field should suffice.
	# MAYBE LATER

	# the link to the post, on Instagram.
	insta_url				=			models.URLField(max_length=1000, blank=False, null=True, default='https://www.instagram.com/')

	timestamp				=			models.DateTimeField(auto_now=False, auto_now_add=True)
	updated					=			models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return(str(self.user) + " " + str(self.insta_id))

################   P R E    S A V E    S T U F F     F O R     S L U G     C R E A T I O N
def create_slug(instance, new_slug=None):
	slug = slugify(instance.blog_title)
	if new_slug is not None:
		slug = new_slug
	qs = blog.objects.filter(blog_slug=slug).order_by("-id")
	exists = qs.exists()
	if exists:
		# the code below, up until return, has been copied from my other project, text2image's code model
	# I remember solving the repetitive problem over there.
		if "_" in slug:
			a = slug.split('_')
			a_list = a[:-1] #remove the last element from this list.
			a = "-".join(a_list)
		else:
			a = slug
		return create_slug(instance, new_slug=new_slug)
	return slug

def create_title(instance, new_title=None):
	# TODO: 
	# Create a script which cuts the string from the first period, and takes the first
	# half as the title, and the rest as the blog post.
	new_title = "This is a sample"

	return new_title

def pre_save_jd_receiver(sender, instance, *args, **kwargs):
	if not instance.blog_title:
		instance.blog_title = create_title(instance)
	if not instance.blog_slug:
		instance.blog_slug = create_slug(instance)

pre_save.connect(pre_save_jd_receiver, sender=blog)
