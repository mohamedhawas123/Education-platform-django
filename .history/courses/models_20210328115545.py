from django.db import models
from django.contrib.auth.models import User



class Course(models.Model):
    owner = models.ForeignKey(User,related_name='courses_created'  ,on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='courses', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug= models.SlugField(max_length=200, unique=True)
    overView = models.TextField()
    created =  models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)