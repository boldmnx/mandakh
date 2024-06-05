from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponse
# from .doctors import Doctor
from manage import doctor1, doctor2, doctor3

def index(request):
    
    return render(request, 'index.html')


def read_doctor(request):
    print("Helooooooooooooooo")
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
        doctor = Doctor.objects.all()
        cutomer = Customer.objects.first()
        cutomer2 = Customer.objects.first()
        cutomer3 = Customer.objects.first()
    
        if Customer.objects.exists():
            if id == 1:
                cutomer.delete()
                doctor1.setter_currentPerson(cutomer)

            elif id == 2:
                cutomer2.delete()
                doctor2.setter_currentPerson(cutomer2)

            elif id == 3:
                cutomer3.delete()
                doctor3.setter_currentPerson(cutomer3)
        return render(request, 'room.html', {
            'doctor': doctor,
            'cutomer': doctor1.getter_currentPerson(), 
            'cutomer2': doctor2.getter_currentPerson(), 
            'cutomer3': doctor3.getter_currentPerson(), 
            })

    elif request.method == 'GET':
        doctor = Doctor.objects.all()
        return render(request, 'room.html', {
            'doctor': doctor,
            'cutomer': doctor1.getter_currentPerson(), 
            'cutomer2': doctor2.getter_currentPerson(), 
            'cutomer3': doctor3.getter_currentPerson(), 
            })
