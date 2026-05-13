from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.template import loader

from .models import Creator, Entry

def creator(request, creator_id):
    creator_object = get_object_or_404(Creator, pk=creator_id)
    context = {
        'creator': creator_object
    }
    return render(request, "creator.html", context)

def entry(request, entry_id):
    entry_object = get_object_or_404(Entry, pk=entry_id)
    context = {
        'entry': entry_object
    }
    return render(request, "entry.html", context)