import profile

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import UserRegisterForm
from django.contrib import messages

# Create your views here.


def login(request):

    return render(request, 'registration/login_original.html')


def tickets(request):
    return render(request, 'tickets.html')


def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            messages.success(request, f'Usuario {email} creado')
            return redirect('login')

    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'registration/registro.html', context)


def profile(request):


    precio = 15
    context = {'precio': precio}

    return render(request, 'registration/profile.html', context)


def feed(request):
    posts = Post.objects.all()
    profiles = Profile.objects.all()
    context = {'posts': posts, 'profiles': profiles}

    return render(request, 'registration/feed.html', context)



