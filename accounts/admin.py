from django.contrib import admin


from .models import insta_ids


class ID_Admin(admin.ModelAdmin):
	list_display = ['insta_id', 'user', 'timestamp', 'updated']
	list_filter = ['insta_id', 'user', 'timestamp', 'updated']
	search_fields = ['insta_id', 'user', 'timestamp', 'updated']

admin.site.register(insta_ids, ID_Admin)


