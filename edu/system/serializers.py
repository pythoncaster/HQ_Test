from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    lessons = serializers.SerializerMethodField()
    owner = serializers.CharField(source='owner.username')

    class Meta:
        model = Product
        fields = ('title', 'owner', 'lessons')

    def get_lessons(self, obj):
        return [lesson.title for lesson in obj.lesson.all()]


class ProductWithAccessCountSerializer(serializers.ModelSerializer):
    access_count = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'title', 'access_count')

    def get_access_count(self, obj):
        return obj.productaccess_set.count()
