from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.utils import reverse_lazy




class StudentRegisterView(CreateView):
    template_name = 'students/student/registeration.html'
    form_class = UserCreationForm
    success_url = 