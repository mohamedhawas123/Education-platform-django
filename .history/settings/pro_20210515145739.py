from settings.local import DATABASES, DEBUG
from .base import *

DEBUG = False


ADMINS = (
    'Saif', 'seifbond77@gmail.com',
)

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': "educa",
       "USER": "educa",
       "PASSWORD": "thugstools"

}
}