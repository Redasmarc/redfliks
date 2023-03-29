from django.contrib import messages
from django.contrib.auth import get_user_model, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.urls import reverse_lazy

User = get_user_model()

@csrf_protect
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        is_error = False
        if User.objects.filter(username=username).exists():
            is_error = True
            messages.error(request, "Sorry! Username is taken.")
        if len(username) == 0:
            is_error = True
            messages.error(request, "Please enter username.")
        if len(email) >0 and User.objects.filter(email=email).exists():
            is_error = True
            messages.error(request, "Sorry! User with this email address already exists.")
        if len(email) == 0:
            is_error = True
            messages.error(request, "Please enter email address")
        if password1 != password2:
            is_error = True
            messages.error(request, "Passwords do not match.")
        if len(password1) ==0 or len(password2) == 0:
            is_error = True
            messages.error(request, "Please enter a password.")
        if not is_error:
            try:
                User.objects.create_user(username=username, email=email, password=password1)
            except Exception as e:
                is_error = True
                messages.error(request, str(e))
        if not is_error:
            messages.success(request, f"Welcome {username}! You have signed up successfully! Please choose the subscription pack for youself.")
            user = authenticate(request, username=username, password=password1)
            login(request, user)
            return redirect(reverse_lazy('shop'))
    return render(request, 'user_profile/register.html')

def shop(request): 
    return(request, 'user_profile/shop.html')
