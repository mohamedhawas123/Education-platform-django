from rest_framework import generics
from .serializers import SubjectSerializer, CourseSerializers
from ..models import Subject, Course
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthenticatation
from rest_framework.permissions import IsAuthenticated

class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer




class ModuleListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers


class CourseEnrollView(APIView):
    authentication_classes = (BasicAuthenticatation, )
    permission_classes = (IsAuthenticated, )

    def post(self, request, pk, format=None):
        course = get_object_or_404(Course, pk=pk)
        course.students.add(request.user)
        return Response({'enrolled': 'ok'})