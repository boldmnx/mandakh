from django.shortcuts import render, redirect
from chat_app.forms import UserForm, UserProfileForm
from chat_app.models import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def index(request):
    if request.user.is_authenticated:
        userid = request.user.id
        profile = UserProfile.objects.get(user_id=userid)
        return render(request, 'index.html', {'profile': profile})
    return render(request, 'index.html')


def edit(request, id):
    if request.method == 'GET':
        usermodel = User.objects.get(id=id)
        profilemodel = UserProfile.objects.get(user_id=usermodel.id)
        userform = UserForm(instance=usermodel)
        userform.fields.pop('password')
        proform = UserProfileForm(instance=profilemodel)
        proform.fields.pop('repassword')
        return render(request, 'edit.html', {'userform': userform, 'proform': proform})
    elif request.method == 'POST':
        usermodel = User.objects.get(id=id)
        profilemodel = UserProfile.objects.get(user_id=usermodel.id)
        userform = UserForm(
            request.POST, instance=usermodel)
        userform.fields.pop('password')
        proform = UserProfileForm(
            request.POST, request.FILES, instance=profilemodel)
        proform.fields.pop('repassword')
        
        if proform.is_valid() and userform.is_valid():
            userform.save()
            if 'user_img' in request.FILES:
                proform.user_img = request.FILES['user_img']
            proform.save()
            return HttpResponseRedirect(reverse('home'))
        return HttpResponse('buruu utga oruulsan bn')


def loged_user(request):
    usermodel = User.objects.all()
    profilemodel = UserProfile.objects.all()
    pairs = zip(usermodel, profilemodel)
    return render(request, 'loged_user.html', {'pairs': pairs})


def remove(request, id):
    usermodel = User.objects.get(id=id)
    usermodel.delete()
    return HttpResponseRedirect(reverse('home'))


def register(request):
    registered = False
    if request.method == 'POST':
        uform = UserForm(request.POST)
        proform = UserProfileForm(request.POST, request.FILES)
        if uform.is_valid() and proform.is_valid():
            if proform.cleaned_data['repassword'] == uform.cleaned_data['password']:
                user = uform.save()
                user.set_password(user.password)
                user.save()

                profile = proform.save(commit=False)
                profile.user = user
                if 'user_img' in request.FILES:
                    profile.user_img = request.FILES['user_img']
                profile.save()
                registered = True
                return HttpResponseRedirect(reverse('login'))
            else:
                return HttpResponse('Нууц үг таарахгүй байна')
        else:
            print(uform.errors, proform.errors)

    else:
        uform = UserForm()
        proform = UserProfileForm()
        return render(request, 'register.html', {'uform': uform, 'proform': proform, 'registered': registered})


def sign(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse('Бүртгэлгүй хэрэглэгч байна.')
        else:
            print("Username: {} and password {}". format(username, password))
            return HttpResponse("Та бүртгэлгүй байна")
    else:
        return render(request, 'login.html')


@login_required
def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def special(e, b):
    if e == b:
        return True
