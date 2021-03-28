from django.db import models
from django.contrib.auth.models import User



class Course(models.Model):
    owner = models.ForeignKey(User,related_name='courses_created'  ,on_delete=models.CASCADE)