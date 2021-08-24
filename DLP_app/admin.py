from django.contrib import admin
from .models import Message, Pattern

# Register your models here.
admin.site.register(Message)
admin.site.register(Pattern)