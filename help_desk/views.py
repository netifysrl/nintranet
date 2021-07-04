from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required



# Create your views here.

@login_required()
def home(request):
    return render(request, 'index.html')

# Temporaneo per profare pagina profile 
@login_required()
def user_profile(request):
    return render(request, 'profile.html')



