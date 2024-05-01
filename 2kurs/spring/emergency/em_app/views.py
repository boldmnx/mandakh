from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def read_doctor(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor.html', {'doctors': doctors})


def read_customer(request):
    if request.method == 'GET':
        cform = CostumerForm()
        customer = Customer.objects.all()
        return render(request, 'customer.html', {'customers': customer, 'cform': cform})
    elif request.method == 'POST':
        cform = CostumerForm(request.POST)
        if cform.is_valid():
            cform.save()
            return redirect('customer')


def room(request, id=None):
    if request.method == 'POST':
    
        if Customer.objects.exists():

            if id == 1:
                cutomer = Customer.objects.first()
                doctor = Doctor.objects.all()
                cutomer.delete()
                return render(request, 'room.html', {'cutomer': cutomer, 'doctor': doctor})
            elif id == 2:

                cutomer2 = Customer.objects.first()
                doctor = Doctor.objects.all()
                cutomer2.delete()
                return render(request, 'room.html', {'cutomer2': cutomer2, 'doctor': doctor})
            elif id == 3:
                cutomer3 = Customer.objects.first()
                doctor = Doctor.objects.all()
                cutomer3.delete()
                return render(request, 'room.html', {'cutomer3': cutomer3, 'doctor': doctor})


    elif request.method == 'GET':
        doctor = Doctor.objects.all()
        return render(request, 'room.html', {'doctor': doctor})
