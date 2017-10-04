from common import *

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'xander-complete', 
        'USER': 'psql',
        'PASSWORD': '',
        'HOST': 'apsql', 
        'PORT': 5432,
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/


OWNER = 'xander-harris'
CV = 'complete'
DIR = 'xander'

STATIC_URL = '/static/xander/'
STATIC_ROOT = '/srv/rsum/xander-complete/static/xander/'
