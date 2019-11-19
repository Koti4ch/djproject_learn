from django.shortcuts import render



def startpage(request):
    return render(request, 'eventgen/event/all_active.html')