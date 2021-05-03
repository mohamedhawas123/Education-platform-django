from django import forms
from django.forms.models import inlineformset_factory
from .models import Course, Module

moduleFormset = inlineformset_factory(
  Course,
 Module,
  fields=['title', 'description'],
  extra=3,
  can_delete=True
)
