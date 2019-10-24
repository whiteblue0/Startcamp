from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login 
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserChangeForm, CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {'form': form, }
    return render(request, 'accounts/auth_form.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            auth_login(request, request.POST)
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/auth_form.html', context)