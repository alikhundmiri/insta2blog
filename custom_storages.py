
# custom_storages.py
from django.conf import settings
from storages.backends.s3boto import S3BotoStorage

# In order for our STATICFILES_STORAGE to have different settings from our DEFAULT_FILE_STORAGE, they need to use two different storage classes
# this file will help create a new filder with different settings in our s3 bucket

class StaticStorage(S3BotoStorage):
    location = settings.CUSTOM_PROJECT_NAME +"/"+ settings.STATICFILES_LOCATION

class MediaStorage(S3BotoStorage):
    location = settings.CUSTOM_PROJECT_NAME +"/"+ settings.MEDIAFILES_LOCATION
