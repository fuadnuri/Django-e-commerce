from .base import *
ALLOWED_HOSTS = []
SECRET_KEY = 'wt!go1iiu4*+yl-^%3m&f95m%15ev!34ck-_7nmtc*&=cgzg_)'
WSGI_APPLICATION = 'drfecommerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
