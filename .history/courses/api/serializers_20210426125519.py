from rest_framework import serializers
from ..models import Subject, Course, Module, Content


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
    # moduels = ModuleSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = ['owner', 'students', 'title', 'subject', 'slug', 'overView', 'created', 'moduels']


    def get_moduels(self, obj):
        return ModuleSerializer(obj.moduels.all(), many=True).data


class ItemRelatedField(serializers.RelatedField):
    
    def to_representation(self, value):
        return value.render()


class ContentSerialisers(serializers.ModelSerializer):

    item = ItemRelatedField(read_only=True)

    class Meta:
        model = Content
        fields = ['order', 'item']


class ModuleWithContentSerialiers(serializers.ModelSerializer):

    contents = ContentSerialisers(many=True)

    class Meta:
        model = Module
        fields = ['Course', 'title', 'description', 'order', 'contents']



class CourseWithContentSerializers(serializers.ModelField):

    moduels = ModuleWithContentSerialiers(many=True)

    class Meta:
        model = Course
        fields = ['owner', 'students', 'title', 'subject', 'slug', 'overView', 'created', 'moduels']



