from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from todo.models import Todo
from todo.serializers import TodoSerializer

# Create your views here.
class TodoViewSet(viewsets.ModelViewSet):
    """
    API viewset for viewing and editing user instances.
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer



def index(request):
    """
    Base view
    """
    todo_list = Todo.objects.all()
    context = {"todos": todo_list}
    return render(request, "todo/index.html", context)


def detail(request, todo_id):
    """
    Detail view
    """
    todo = get_object_or_404(Todo, pk=todo_id)
    context = {"todo": todo}
    return render(request, "todo/detail.html", context)
