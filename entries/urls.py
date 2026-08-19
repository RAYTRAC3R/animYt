from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # ex: /entry/5/
    path('entry/<int:entry_id>/', views.entry, name='entry'),
    # ex: /creator/5/
    path("creator/<int:creator_id>/", views.creator, name="creator"),
    # ex: /character/5/
    path("character/<int:character_id>/", views.character, name="character"),
]