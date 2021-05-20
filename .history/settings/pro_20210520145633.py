from settings.local import DATABASES, DEBUG
from .base import *

DEBUG = False


ADMINS = (
    'Saif', 'seifbond77@gmail.com',
)

ALLOWED_HOSTS = ['educaproject.com', 'www.educaproject.com']

DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': "educaa",
       "USER": "educa",
       "PASSWORD": "panzer123",
       "HOST": 'localhost',
       "PORT": '',


}
}


#don't forget to add host and port 