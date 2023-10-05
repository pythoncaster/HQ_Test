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
    percent = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'title', 'access_count', 'percent')

    def get_access_count(self, obj):
        return obj.productaccess_set.count()

    def get_percent(self, obj):
        users_count = User.objects.count()
        if users_count > 0:
            return (obj.productaccess_set.count() / users_count) * 100
        else:
            return 0
