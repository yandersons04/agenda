from django.shortcuts import render, get_object_or_404, redirect
from . models import Event, Comment
from django.utils.timezone import localdate
from django.core.paginator import Paginator, InvalidPage
from django.http import HttpResponse
from django.views.defaults import bad_request, server_error
from datetime import datetime, timedelta

ITEMS_PER_PAGE = 5

# Create your views here.

def index(request):
    """Exibe a página principal da aplicação"""
    context = {
        'hide_new_button': True,
        'prorities': Event.priorities_list,
        'today': localdate(),
    }
    return render(request, 'index.html', context)

""" Exibe todos os eventos em uma única página, recebe o número da pagina a ser visualizada: via GET"""
def all(request):
    page = request.GET.get('page', 1)
    paginator = Paginator(Event.objects.all(), ITEMS_PER_PAGE)
    total = paginator.count

    try:
        events = paginator.page(page)
    except InvalidPage:
        events = paginator.page(1)

    context = {
        'events': events,
        'total': total,
        'priorities': Event.priorities_list,
        'today': localdate(),
    }
    return render(request, 'events.html', context)

""" Visualização dos eventos de um determinado dia, recebe a data em formato ano/mes/dia como parâmetro """
def day(request, year:int, month:int, day:int):
    day = datetime(year, month, day)
    events = Event.objects.filter(date='{%Y-%m-%d}'.format(day)).order_by('-priority', 'event')
    context = (
        'today': localdate()
        'day': day,
        'events': events,
        'next': day + timedelta(days=1),
        'previous': day - timedelta(days=1),
        priorities: Event.priorities_list
    )
    return render(request, day.html, context)