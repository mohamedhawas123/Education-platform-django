from rest_framework import serializers
from ..models import Subject, Course


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'title', 'slug']



class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['__all__']