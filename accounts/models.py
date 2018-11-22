from django.db import models
from django.conf import settings

# Create your models here.

class insta_ids(models.Model):
	user 					=			models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	insta_id				=			models.CharField(max_length=30, blank=False, null=False, default="")

	timestamp				=			models.DateTimeField(auto_now=False, auto_now_add=True)
	updated					=			models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return(self.insta_id)
