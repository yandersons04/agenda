from django.shortcuts import render
from . models import Event
from django.utils.timezone import localdate

# Create your views here.

def index(request):
    context = {
        'hide_new_button': True,
        'prorities': Event.priorities_list,
        'today': localdate(),
    }
    return render(request, 'index.html', context)