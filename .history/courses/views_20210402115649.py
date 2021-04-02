from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Course



class ManagecourseListView(DetailView):
    model = Course
    template_name = 'courses/manage/course/list.html'
    
    def get_q
