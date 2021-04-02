from django.shortcuts import render, reverse_lazy
from django.views.generic import ListView
from .models import Course



# class ManagecourseListView(ListView):
#     model = Course
#     template_name = 'courses/manage/course/list.html'
    
#     def get_queryset(self):
#         qs = super().get_queryset()
#         return qs.filter(owner=self.request.user)


class Ownermixins(object):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)


class OwnerEditMixins(object):
    def form_valid(self, form):
        form.instance.owner =  self.request.user
        return super().form_valid(form)


class OwnerCourseMixin(Ownermixins):
    model = Course 
    fields =  ['subject', 'title', 'slug', 'overview']
    success_url = reverse_lazy('manage_course_list')

class OwnerCourseEditMixn(OwnerCourseMixin, OwnerEditMixins ):
    template_name = 'courses/manage/course/form.html'
        