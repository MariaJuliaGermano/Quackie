from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
import templates

def landing(request):
    return render(request, 'core/landing.html')
