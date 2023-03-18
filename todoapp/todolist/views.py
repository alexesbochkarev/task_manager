from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect


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


# class TodoUpdateView(View):
#     model = ToDo
#     fields = ['is_complete']
#     template_name='todolist/index.html'
#     success_url = reverse_lazy('todolist:index')


def update(request, pk):
        todo = ToDo.objects.get(id=pk)
        todo.is_complete = not todo.is_complete
        todo.save()
        return redirect('todolist:index')

def delete(request, pk):
        todo = ToDo.objects.get(id=pk)
        todo.is_complete = not todo.is_complete
        todo.delete()
        return redirect('todolist:index')