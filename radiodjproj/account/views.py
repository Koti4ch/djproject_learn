from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from account.forms import LoginForm

# Create your views here.

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
