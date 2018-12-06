from django.db import models
from django.conf import settings

# Create your models here.

class insta_account(models.Model):
	# a paid user can have up to 5 instagram accounts connected. This is where we store insta bio, user, 
	# insta_id, 
	user 					=			models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	insta_id				=			models.CharField(max_length=30, blank=False, null=False, default="")
	insta_username			=			models.CharField(max_length=30, blank=False, null=False, default="")
	bio						=			models.TextField(max_length=150, blank=True, null=True, default="user bio here")

	# add a field to enable user's custom bio, or load directly from Instagram. A simple boolean field should suffice.
	timestamp				=			models.DateTimeField(auto_now=False, auto_now_add=True)
	updated					=			models.DateTimeField(auto_now=True, auto_now_add=False)
	def __str__(self):
		return(self.insta_id)

