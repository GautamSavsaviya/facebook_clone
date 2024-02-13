from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm
from .models import Profile


# Create your views here.
def register_user(request):
    if request.user.is_authenticated:
        
        messages.warning(request, "You are registered..!")
        return redirect("core:feed")

    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()
        full_name = form.cleaned_data.get('full_name')
        phone = form.cleaned_data.get('phone')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')

        user = authenticate(email=email, password=password)
        login(request, user)

        messages.success(
            request, f'Hi {full_name}, your account is created successfully.')

        profile = Profile.objects.get(user=request.user)
        profile.phone = phone
        profile.save()

        return redirect('core:feed')
    
    context = {
        'form':form
    }

    return render(request, 'user_auth/signup.html', context)