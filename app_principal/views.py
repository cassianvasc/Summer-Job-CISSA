from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# Home pós-login
@login_required
def home(request):
    return render(request, 'app_principal/homehtml.html')


@login_required
def denuncia(request):
    return render(request, 'app_principal/denuncia.html')
