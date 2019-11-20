from django.shortcuts import render
from django.contrib import messages
from account.forms import RegistrationUserForm



def startpage(request):
    messages.success(request, 'test SUCCESS message!')
    messages.debug(request, 'test DEBUG message!')
    messages.warning(request, 'test WARNING message!')
    messages.error(request, 'test ERROR message!')
    messages.info(request, 'test INFO message!')
    return render(request, 'eventgen/event/all_active.html')