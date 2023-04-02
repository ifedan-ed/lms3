import environ                           # new
from pathlib import Path

env = environ.Env()                      # new


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='django-insecure-$lko+#jpt#ehi5=ms9(6s%&6fsg%r2ag2xu_2zj1ibsj$pckud')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DJANGO_DEBUG", True)

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=[])

import os                                                                            # new

MIDDLEWARE = [
   'django.middleware.security.SecurityMiddleware',
   'whitenoise.middleware.WhiteNoiseMiddleware',                                     # new
   # ...
]

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')                                       # new

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"      # new

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')                                      # new
MEDIA_URL = '/media/'                                                             # new

if 'AWS_STORAGE_BUCKET_NAME' in env:                                              # new
    AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
    AWS_S3_REGION_NAME = env('AWS_S3_REGION_NAME')
    AWS_DEFAULT_ACL = 'public-read'
    AWS_S3_FILE_OVERWRITE = False

    MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


if "DATABASE_URL" in env:
    DATABASES['default'] = env.db('DATABASE_URL')
    DATABASES["default"]["ATOMIC_REQUESTS"] = True

