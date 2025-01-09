from django.shortcuts import render
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
    return render(request, "todo/_base.html")
