from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect, get_object_or_404, redirect


from .models import ToDo
from .forms import TodoForm, UpdateCommentForm


class TodoFilterView:

    def get_complete(self):
        return ToDo.objects.filter(is_complete=True)

    def get_not_complete(self):
        return ToDo.objects.filter(is_complete=False)


class IndexListView(TodoFilterView, ListView):
    
    context_object_name = 'task'
    template_name='todolist/index.html'

    def get_queryset(self):
        return ToDo.objects.order_by('-id')[0:9]

class TodoCreateView(CreateView):
    model = ToDo
    form_class = TodoForm
    template_name='todolist/create.html'
    
    success_url = "/detail/{id}"


class CompleteListView(TodoFilterView, ListView):
    model = ToDo
    template_name='todolist/complete.html'


class CompleteNotListView(TodoFilterView, ListView):
    model = ToDo
    template_name='todolist/complete_not.html'


class SearchNumberView(TodoFilterView, ListView):
    """Поиск по номеру телефона"""
    template_name='todolist/search_number.html'
    def get_queryset(self):
        queryset = ToDo.objects.filter(number__in=self.request.GET.getlist("number"))
        return queryset


class SearchDateView(TodoFilterView, ListView):
    """Поиск по дате"""
    template_name='todolist/search_date.html'
    def get_queryset(self):
        queryset = ToDo.objects.filter(datatime__in=self.request.GET.getlist("datatime"))
        return queryset


class TodoDetailview(TodoFilterView, DetailView):
     model = ToDo
     template_name='todolist/todo_detail.html'


class TodoUpdateView(UpdateView):
    model = ToDo
    template_name='todolist/create.html'
    form_class = UpdateCommentForm
    success_url = "/detail/{id}"


def update(request, pk):
        todo = ToDo.objects.get(id=pk)
        todo.is_complete = not todo.is_complete
        todo.save()
        return redirect(request.META.get('HTTP_REFERER'))

def delete(request, pk):
        todo = ToDo.objects.get(id=pk)
        todo.is_complete = not todo.is_complete
        todo.delete()
        return redirect('todolist:index')

