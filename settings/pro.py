from settings.local import DATABASES, DEBUG
from .base import *

DEBUG = False


ADMINS = (
    'saiff', 'seifbond77@gmail.com',
)

ALLOWED_HOSTS = ['learnit-platform.herokuapp.com', '127.0.0.1']

DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': "d7o5v2edrh59q8",
       "USER": "easnvcidlpsron",
       "PASSWORD": "873a1d9b222aa13422f21e974d4df943229660ecb6619885a4121fc271e9b3a2",
       "HOST": 'ec2-35-171-171-27.compute-1.amazonaws.com',
       "PORT": '5432',


}
}


SECURE_SSL_REDIRECT = True

CSRF_COOKIE_SECURE = True

#don't forget to add host and port 
