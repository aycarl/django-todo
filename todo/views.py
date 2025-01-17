from django.http import HttpResponse
from django.views import generic
from django.views.decorators.http import require_GET, require_http_methods
from rest_framework import viewsets
from todo.models import Todo
from todo.serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    """
    API viewset for viewing and editing user instances.
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class IndexView(generic.ListView):
    """
    Base view
    """
    template_name = "todo/htmx-index.html"
    context_object_name = "todos"

    def get_queryset(self):
        return Todo.objects.all()


@require_http_methods(["PUT"])
def toggle_todo(request, pk):
    """
    Toggle the completed state of a todo
    """
    todo = Todo.objects.get(pk=pk)
    todo.completed = not todo.completed
    todo.save()
    return HttpResponse(status=204)


@require_GET
def favicon(request) -> HttpResponse:
    return HttpResponse(
        (
                '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">'
                + '<text y=".9em" font-size="90">🦊</text>'
                + "</svg>"
        ),
        content_type="image/svg+xml",
    )
