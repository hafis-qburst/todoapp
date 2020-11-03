from django.shortcuts import render, redirect
from .models import TodoList
from .forms import TodoListForm
from django.views.decorators.http import require_POST
# Create your views here.

def main_view(request):
    todo_items = TodoList.objects.order_by('id')
    form = TodoListForm()
    context = {'todo_items': todo_items, 'form': form}
    return render(request, 'todolist/main.html', context)


@require_POST
def add_todo_item(request):
    form = TodoListForm(request.POST)
    if form.is_valid():
        new_todo = TodoList(text=request.POST['text'])
        new_todo.save()
    return redirect('main')


def completed_todo(request, todo_id):
    todo = TodoList.objects.get(pk=todo_id)
    todo.completed = not todo.completed
    todo.save()
    return redirect('main')

def delete_completed(request):
    todo = TodoList.objects.all()
    for item in todo:
        if item.completed:
            item.delete()
    return redirect('main')

def delete_all(request):
    TodoList.objects.all().delete()
    return redirect('main')
