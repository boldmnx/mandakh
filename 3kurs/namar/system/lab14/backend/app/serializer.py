from rest_framework import serializers
from .models import Student

class StudendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'