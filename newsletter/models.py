from django.db import models

# Create your models here.
# Create your models here.
class newsletter_list(models.Model):
	
	THRESHOLD_LIST = (
		('free-version', 'FREE'),
		('paid-15', '15USD'),
		('paid-30', '30USD'),
		)

	email_address 			=			models.EmailField(max_length=254, blank=False, null=False)
	user_name				=			models.CharField(max_length=200, blank=True, null=True)
	threshold				=			models.CharField(max_length=20, choices=THRESHOLD_LIST, default=THRESHOLD_LIST[0][0])
	
	timestamp				=			models.DateTimeField(auto_now=False, auto_now_add=True)
	updated					=			models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return(self.email_address + " " + self.user_name)

	class Meta:
		ordering	 		=			["-timestamp", "-updated"]
		verbose_name 		= 			"Interested Person"
		verbose_name_plural = 			"Interested People"
