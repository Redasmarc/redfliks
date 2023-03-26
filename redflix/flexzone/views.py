from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import models

# Create your views here.

@login_required
def index(request):
    return render(request, 'flexzone/index.html')