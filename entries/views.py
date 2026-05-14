from django.db.models import F, Prefetch
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.template import loader

from .models import Creator, Entry

def index(request):
    context = {
        'creators': list(Creator.objects.all()),
        'memes': list(Entry.objects.all())
    }
    return render(request, "index.html", context)

def creator(request, creator_id):
    creator_object = get_object_or_404(Creator, pk=creator_id)
    context = {
        'creator': creator_object,
        'memes': list(creator_object.memes_made.all())
    }
    return render(request, "creator.html", context)

def entry(request, entry_id):
    entry_object = get_object_or_404(Entry, pk=entry_id)
    related_objects = []
    for x in list(entry_object.related_memes.all()):
        if x != entry_object and x!= entry_object.original_meme:
            related_objects.append(x)
    context = {
        'entry': entry_object,
        'related_entries': related_objects,
        'by_creator': list(entry_object.creator.memes_made.all())
    }
    return render(request, "entry.html", context)