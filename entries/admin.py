from django.contrib import admin

from .models import Creator, Character, Entry

admin.site.register(Creator)
admin.site.register(Character)
admin.site.register(Entry)