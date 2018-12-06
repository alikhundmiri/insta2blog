from django.contrib import admin

from .models import blog
# Register your models here.


class blog_Admin(admin.ModelAdmin):
	list_display = ['insta_id', 'user', 'timestamp', 'updated']
	list_filter = ['insta_id', 'user', 'timestamp', 'updated']
	search_fields = ['insta_id', 'user', 'timestamp', 'updated']

admin.site.register(blog, blog_Admin)

