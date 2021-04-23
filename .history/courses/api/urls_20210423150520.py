from django.urls import path
from .views import SubjectListView, SubjectDetailView

app_name = 'courses'

urlpatterns = [
    path('subjects/', SubjectListView.as_view(), name="subject_list" ),
    path('subjects/<pk>/', SubjectDetailView.as_view(), name="subject_detail")
]
