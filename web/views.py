from django.shortcuts import render
from django.http.response import HttpResponse

from posts.models import Event

def index(request):
    events = Event.objects.filter(is_deleted=False)

    context = {
        "title": "Home Page",
        "events": events
    }
    return render(request, 'web/index.html', context=context)
