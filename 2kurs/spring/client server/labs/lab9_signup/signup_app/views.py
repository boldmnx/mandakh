from django.shortcuts import render, redirect
from signup_app.forms import SignupForm
from signup_app.models import Signup
# Create your views here.


def signup(request):
    if request.method == 'POST':
        signupForm = SignupForm(request.POST)
        if signupForm.is_valid():
            if signupForm.cleaned_data['password'] == signupForm.cleaned_data['repassword']:
                signupModel = Signup.objects.create(
                    fname=signupForm.cleaned_data['fname'],
                    lname=signupForm.cleaned_data['lname'],
                    email=signupForm.cleaned_data['email'],
                    password=signupForm.cleaned_data['password']
                )
                signupModel.save()
                return redirect('home')
            else:
                request.session['msg'] = 'nuuts ug taarahgui bna'
                return render(request, 'signup.html', {'signupForm': signupForm, 'msg': 'nuuts ug taarahgui bna'})
    elif request.method == 'GET':
        signupForm = SignupForm()
        return render(request, 'signup.html', {'signupForm': signupForm})


def index(request):
    signupModels = Signup.objects.all()
    return render(request, 'index.html', {"signup": signupModels})
