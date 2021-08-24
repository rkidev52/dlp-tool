from django.contrib import admin
from django.urls import path, include
from .views import indexView, event_hook, SearchPatternsView

app_name = 'dlp'

urlpatterns = [
    path('', indexView, name="index"),
    path('search/patterns', SearchPatternsView, name="searcher"),
    path('event/hook', event_hook, name='event_hook'),
]
