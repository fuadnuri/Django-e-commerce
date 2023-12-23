import os
from .base import *
ALLOWED_HOSTS = []
SECRET_KEY = os.environ.get('SECRET_KEY')
WSGI_APPLICATION = 'drfecommerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
