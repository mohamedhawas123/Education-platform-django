from django.urls import path
from .views import SubjectListView, SubjectDetailView, ModuleListView

app_name = 'courses'

urlpatterns = [
    path('subjects/', SubjectListView.as_view(), name="subject_list" ),
    path('subjects/<pk>/', SubjectDetailView.as_view(), name="subject_detail"),
    path('courses/', ModuleListView.as_view(), name="course_list" ),
    path('courses/<pk>/enroll/', views.CourseEnrollView.as_view(), name='course_enroll'),
]
