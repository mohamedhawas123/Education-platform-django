from django.db import models
from django.contrib.auth.models import User



class Course(models.Model):
    owner = models.ForeignKey()