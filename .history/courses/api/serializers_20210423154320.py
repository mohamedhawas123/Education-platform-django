from rest_framework import serializers
from ..models import Subject, Course, Module


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'title', 'slug']


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['order', 'title', 'description']


class CourseSerializers(serializers.ModelSerializer):

    moduels = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['owner', 'students', 'title', 'subject', 'slug', 'overView', 'created', 'moduels']


    def get_moduels(self, obj):
        return ModuleSerializer(obj.moduels.all(), many=True).data