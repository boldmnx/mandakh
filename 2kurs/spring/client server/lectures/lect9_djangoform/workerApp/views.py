from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.
# cleaned_data


def workerCreate(request):
    if request.method == 'GET':
        wform = WorkerForm
        return render(request, 'worker/workerCreate.html', {'wform': wform})
    elif request.method == 'POST':
        sub_form = WorkerForm(request.POST)
        w = Worker()
        if sub_form.is_valid():
            w.wfname = sub_form.cleaned_data['wfname']
            w.wlname = sub_form.cleaned_data['wlname']
            w.wgender = sub_form.cleaned_data['wgender']
            w.wphone = sub_form.cleaned_data['wphone']
            w.bid = sub_form.cleaned_data['branch']
            w.save()
