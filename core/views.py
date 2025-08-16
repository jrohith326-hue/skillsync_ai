from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm, ProfileForm
from .models import CareerPath, Course
from django.contrib.auth.decorators import login_required
from .ai_engine import recommend_careers
from django.contrib import messages  # ✅ Added for feedback messages
from .forms import RegisterForm, ProfileForm

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)  # ✅ Added request.FILES for file uploads
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration successful! You can now log in.')  # ✅ Success message
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')  # Optional: error message
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')  # Optional feedback
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard_view(request):
    user_profile = request.user.userprofile
    user_skills = user_profile.skills.all()
    
    recommendations = recommend_careers(user_skills)
    
    return render(request, 'dashboard.html', {
        'recommendations': recommendations
    })

@login_required
def update_profile_view(request):
    profile = request.user.userprofile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)  # ✅ Support file updates
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')  # ✅ Feedback
            return redirect('dashboard')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profile.html', {'form': form})

