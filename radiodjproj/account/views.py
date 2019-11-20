from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from account.forms import LoginForm, RegistrationUserForm, UserEditForm, UserProfileEditForm
from account.models import UserProfile

# Create your views here.

def registration_user(request):
    if request.method == 'POST':
        registration_form = RegistrationUserForm(request.POST)
        if registration_form.is_valid():
            new_user = registration_form.save(commit=False)
            new_user.set_password(registration_form.cleaned_data['password'])
            UserProfile.objects.create(user=new_user)
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        registration_form = RegistrationUserForm()
    return render(request, 'account/register.html', {'registration_form': registration_form})

@login_required
def edit_user_info(request):
    if request.method == 'POST':
        user_edit_form = UserEditForm(instance=request.user, data=request.POST)
        profile_edit_form = UserProfileEditForm(instance=request.user.userprofile, data=request.POST,
                                                files=request.FILES,
                                                )
        if user_edit_form.is_valid() and profile_edit_form.is_valid():
            user_edit_form.save()
            profile_edit_form.save()
            messages.success(request, f'User {request.user.username} was apdated successfully!')
    else:
        user_edit_form = UserEditForm(instance=request.user)
        profile_edit_form = UserProfileEditForm(instance=request.user.userprofile)
    return render(request, 'account/edituserinfo.html', {'user_edit_form': user_edit_form,
                                                         'profile_edit_form': profile_edit_form,
                                                         })


@login_required
def dashboard(request):
    messages.error(request, 'Test error message!')
    messages.info(request, 'Test info message!')
    messages.warning(request, 'Test warning message!')
    messages.success(request, 'Test success message!')
    messages.debug(request, 'Test debug message!')
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
                messages.success(request, 'Authenticate successfully!')
                return HttpResponse('Authenticate successfully')
            else:
                return HttpResponse('Disable account!')
        else:
            return HttpResponse('Invalid login or password!')
    else:
        form = LoginForm()
    return render(request, 'account/user_login.html', {'form': form})
