from django.contrib import admin
from .models import ToDo, Comment

admin.site.register(Comment)
admin.site.register(ToDo)
