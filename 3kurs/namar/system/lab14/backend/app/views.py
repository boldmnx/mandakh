from django.shortcuts import render
from rest_framework import generics
from .models import Student
from .serializer import StudendSerializer

# Create your views here.
class StudentGetCreate (generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudendSerializer
class StudentUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudendSerializer


