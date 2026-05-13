from django.contrib import admin

from .models import Creator, Entry

admin.site.register(Creator)
admin.site.register(Entry)