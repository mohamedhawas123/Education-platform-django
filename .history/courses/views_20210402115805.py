from django.shortcuts import render
from django.views.generic import ListView
from .models import Course



class ManagecourseListView(ListView):
    model = Course
    template_name = 'courses/manage/course/list.html'
    
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(ownder=self.request.user)
