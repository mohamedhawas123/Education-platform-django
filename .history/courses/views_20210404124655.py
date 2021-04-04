from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Course
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.base import TemplateResponseMixin, View
from .forms import moduleFormset



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


class CourseModuleUpdateView(TemplateResponseMixin, View):
    template_name = 'courses/manage/module/formset.html'
    course = None

    def get_formset(self, data=None):
        return moduleFormset(instance=self.course, data=data)
    
    def dispatch(self, request, pk):
        self.course = get_object_or_404(Course, id=pk, owner=request.user)
        return super().dispatch(request, pk)

    
    def get(self, request, *args, **kwargs):
        formset = self.get_formset()
        return self.render_to_response({'course': self.course, 'formset': format})