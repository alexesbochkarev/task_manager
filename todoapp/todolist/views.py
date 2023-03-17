from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView


from .models import ToDo
from .forms import TodoForm


class IndexListView(ListView):
    model = ToDo
    context_object_name = 'task'
    template_name='todolist/index.html'


class TodoCreateView(CreateView):
    model = ToDo
    form_class = TodoForm
    template_name='todolist/create.html'
    success_url = reverse_lazy('todolist:index')