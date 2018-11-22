from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
def upload_location(Post, filename):
    return "%s/%s/%s" %(Post.app_name,Post.user, filename)

class Post(models.Model):
    app_name = "Blogs"
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)

    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=300)
    detail = models.TextField(max_length=2200)
    image = models.ImageField(
        upload_to=upload_location,
        null = True,
        blank = True,
        height_field = "height_field",
        width_field = "width_field",
    )
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())

    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blogs:detail", kwargs={"slug" : self.slug})

    class Meta:
        ordering = ["-timestamp", "-updated"]

