from django.db import models
from django.conf import settings

from accounts.models import insta_account


class blog(models.Model):
	# a paid user can have up to 5 instagram accounts connected. This is where we store insta bio, user, 
	# insta_id, 
	user 					=			models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	# each blog post belongs to a single insta_account. each insta2blog user can have max 5 insta_accounts 
	insta_id				=			models.ForeignKey(insta_account, on_delete=models.CASCADE)
	blog_post				=			models.TextField(max_length=2200, blank=True, null=True, default="user bio here")
	link_in_bio				=			models.URLField(max_length=1000, blank=True, null=True)
	# add a field to enable user's custom bio, or load directly from Instagram. A simple boolean field should suffice.
	timestamp				=			models.DateTimeField(auto_now=False, auto_now_add=True)
	updated					=			models.DateTimeField(auto_now=True, auto_now_add=False)
	def __str__(self):
		return(self.insta_id)

