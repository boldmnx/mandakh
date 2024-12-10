from rest_framework import serializers
from .models import Student


class StudendSerializer(serializers.ModelSerializer):

    address = serializers.CharField(required=False, allow_blank=True)
    stfname = serializers.CharField(required=False, allow_blank=True)
    stcode = serializers.CharField(required=False, allow_blank=True)
    born = serializers.CharField(required=False, allow_blank=True,allow_null=True)
    email = serializers.CharField(required=False, allow_blank=True)
    phone = serializers.CharField(required=False, allow_blank=True)
    username = serializers.CharField(required=False, allow_blank=True)
    stlname = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = Student
        fields = '__all__'
