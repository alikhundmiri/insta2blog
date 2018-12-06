from django.contrib import admin


from .models import insta_account


class ID_Admin(admin.ModelAdmin):
	list_display = ['insta_id', 'user', 'timestamp', 'updated']
	list_filter = ['insta_id', 'user', 'bio', 'timestamp', 'updated']
	search_fields = ['insta_id', 'user', 'bio', 'timestamp', 'updated']

admin.site.register(insta_account, ID_Admin)


