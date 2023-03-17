from todolist.forms import TodoForm

def get_context_data(request):
    context = {
        'todo': TodoForm()
    }
    return context