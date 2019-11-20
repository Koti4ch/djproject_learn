from django.shortcuts import render
from account.forms import RegistrationUserForm



def startpage(request):
    return render(request, 'eventgen/event/all_active.html')