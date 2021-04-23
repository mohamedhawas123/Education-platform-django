from rest_framework import generics
from .serializers import SubjectSerializer, CourseSerializers
from ..models import Subject, Course
from rest_framework.views import APIView

class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer




class ModuleListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers


class CourseEnrollView(APiView)