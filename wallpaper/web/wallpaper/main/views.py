from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from .forms import UserRegistrationForm, UserLoginForm, UserProfileUpdateForm
from .models import UserProfile


def home(request):
    """Home page view"""
    return render(request, "index.html")


@require_http_methods(["GET", "POST"])
def register(request):
    """User registration view"""
    if request.user.is_authenticated:
        return redirect('main_app:home')
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('main_app:login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = UserRegistrationForm()
    
    context = {'form': form}
    return render(request, 'auth/register.html', context)


@require_http_methods(["GET", "POST"])
def user_login(request):
    """User login view"""
    if request.user.is_authenticated:
        return redirect('main_app:home')
    
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.get_full_name() or user.username}!')
            return redirect('main_app:home')
        else:
            messages.error(request, 'Invalid username/email or password.')
    else:
        form = UserLoginForm()
    
    context = {'form': form}
    return render(request, 'auth/login.html', context)


@login_required(login_url='main_app:login')
@require_http_methods(["POST"])
def user_logout(request):
    """User logout view"""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('main_app:login')


@login_required(login_url='main_app:login')
@require_http_methods(["GET", "POST"])
def profile(request):
    """User profile view"""
    user = request.user
    
    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('main_app:profile')
        else:
            messages.error(request, 'Error updating profile.')
    else:
        form = UserProfileUpdateForm(instance=user)
    
    context = {
        'form': form,
        'user': user
    }
    return render(request, 'auth/profile.html', context)


@login_required(login_url='main_app:login')
def profile_view(request):
    """View user profile (read-only)"""
    context = {'profile_user': request.user}
    return render(request, 'auth/profile_view.html', context)

