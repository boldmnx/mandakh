from django.shortcuts import render, redirect
import sqlite3 as sql
from .forms import BranchForm
from .models import Branch
# Create your views here.


def read_branch(request):
    if request.method == 'GET':
        bForm = BranchForm()
        bModels = Branch.objects.all()
        return render(request, 'read_branch.html', {'branches': bModels, 'bForm': bForm,
                                                    'title': 'Read and add branches page'})
    elif request.method == 'POST':
        bForm = BranchForm(request.POST)
        bModel = Branch()
        if bForm.is_valid():
            bModel.bname = bForm.cleaned_data['bname']
            bModel.save()
        return redirect('/branch')


def update_branch(request, bid):
    bModel = Branch.objects.get(id=bid)
    if request.method == 'GET':
        return render(request, 'update_branch.html', {'branch': bModel})
    elif request.method == 'POST':
        bname = request.POST.get('bname')
        bModel.bname = bname
        bModel.save()
        return redirect('{%url "rBranch"%}')


def delete_branch(request, bid):
    bModel = Branch.objects.get(id=bid)
    bModel.delete()
    return redirect('/branch')
