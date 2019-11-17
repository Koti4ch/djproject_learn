from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from account.forms import LoginForm, RegistrationUserForm

# Create your views here.

def registration_user(request):
    if request.method == 'POST':
        registration_form = RegistrationUserForm(request.POST)
        if registration_form.is_valid():
            new_user = registration_form.save(commit=False)
            new_user.set_password(registration_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        registration_form = RegistrationUserForm()
    return render(request, 'account/register.html', {'registration_form': registration_form})

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cb = form.cleaned_data
            user = authenticate(request,
                                username=cb['username'],
                                password=cb['password']
                                )
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('Authenticate successfully')
            else:
                return HttpResponse('Disable account!')
        else:
            return HttpResponse('Invalid login or password!')
    else:
        form = LoginForm()
    return render(request, 'account/user_login.html', {'form': form})
