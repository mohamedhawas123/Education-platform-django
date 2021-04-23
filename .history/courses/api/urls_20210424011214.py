from django.urls import path, include
from .views import SubjectListView, SubjectDetailView, CourseEnrollView
from rest_framework import routers
from . import views


app_name = 'courses'

router = routers.DefaultRouter()
router.register('courses', views.CourseViewList)

urlpatterns = [
    path('subjects/', SubjectListView.as_view(), name="subject_list" ),
    path('subjects/<pk>/', SubjectDetailView.as_view(), name="subject_detail"),
    # path('courses/', ModuleListView.as_view(), name="course_list" ),
    path('', include(router.urls)),
  #  path('courses/<pk>/enroll/', CourseEnrollView.as_view(), name='course_enroll'),
]
