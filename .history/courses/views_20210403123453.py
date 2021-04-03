from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Course
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy



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


class OwnerCourseMixin(Ownermixins, LoginRequiredMixin, PermissionRequiredMixin):
    model = Course 
    fields =  ['subject', 'title', 'slug', 'overView']
    success_url = reverse_lazy('manage_course_list')



class OwnerCourseEditMixn(OwnerCourseMixin, OwnerEditMixins ):
    template_name = 'courses/manage/course/form.html'



class ManageCourseListView(OwnerCourseEditMixn, ListView):
    template_name= 'courses/manage/course/list.html'
    permission_required = 'courses.view_course'



class CourseCreateView(OwnerCourseEditMixn, CreateView):
    permission_required = 'courses.add_course'




class CourseUpdateView(OwnerCourseEditMixn, UpdateView):
    permission_required = 'courses.change_course'





class CourseDeleteView(OwnerCourseMixin, DeleteView):
    template_name = 'courses/manage/course/delete.html'
    permission_required = 'courses.delete_course'
    
    def  get_queryset(self):
        return super().get_queryset()
    