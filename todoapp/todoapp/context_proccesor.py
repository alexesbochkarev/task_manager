from todolist.forms import TodoForm, CommentsFormModel


def get_context_data(request):
    context = {
        'todo_create': TodoForm(),
        'comment_create': CommentsFormModel(),
    }
    return context