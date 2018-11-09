from django.contrib import admin

# Register your models here.

from .models import newsletter_list


class NewsletterAdmin(admin.ModelAdmin):
	list_display = ['email_address', 'user_name', 'threshold', 'timestamp', 'updated']
	list_filter = ['email_address', 'user_name', 'threshold', 'timestamp', 'updated']
	search_fields = ['email_address', 'user_name', 'threshold', 'timestamp', 'updated']
	
	class Meta:
		model = newsletter_list

admin.site.register(newsletter_list, NewsletterAdmin)