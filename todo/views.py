from django.http import HttpResponse
from django.shortcuts import render  # Added for rendering partials
from django.views import generic
from django.views.decorators.http import require_GET, require_http_methods, require_POST  # Added require_POST
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
        # Sort by completion status (False then True), then by creation date (newest first)
        return Todo.objects.all().order_by('completed', '-created_at')


@require_http_methods(["POST"])  # Changed from PUT to POST for hx-post
def toggle_todo(request, pk):
    """
    Toggle the completed state of a todo and return the re-sorted list of todos.
    """
    todo = Todo.objects.get(pk=pk)
    todo.completed = not todo.completed
    todo.save()

    # Fetch all todos with the desired sorting
    todos = Todo.objects.all().order_by('completed', '-created_at')
    return render(request, "todo/_todo_list.html", {"todos": todos})


@require_POST
def create_todo(request):
    """
    Create a new todo and return the full todo list to maintain proper sorting.
    """
    title = request.POST.get("title")
    content = request.POST.get("content")
    if title:
        Todo.objects.create(title=title, content=content)
        # Return the full todo list with proper sorting
        todos = Todo.objects.all().order_by('completed', '-created_at')
        return render(request, "todo/_todo_list.html", {"todos": todos})
    return HttpResponse(status=400)  # Bad request if title is missing


@require_http_methods(["DELETE"])
def delete_todo(request, pk):
    """
    Delete a todo and return an empty response.
    """
    try:
        todo = Todo.objects.get(pk=pk)
        todo.delete()
        return HttpResponse(status=200)  # OK, HTMX will remove the element
    except Todo.DoesNotExist:
        return HttpResponse(status=404)  # Not Found


@require_GET
def get_todo_form(request):
    """
    Return the modal form for creating a new todo.
    """
    return render(request, "todo/_todo_form_modal.html")


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
