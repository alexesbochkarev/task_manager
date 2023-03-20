from todolist.forms import TodoForm, UpdateCommentForm


def get_context_data(request):
    context = {
        'todo_create': TodoForm()
    }
    return context