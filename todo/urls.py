from django.urls import include, path
from rest_framework import routers

from todo.views import TodoViewSet, index, detail


app_name = 'todo'
router = routers.DefaultRouter()
router.register(r'todos', TodoViewSet)

urlpatterns = [
    path('', index, name='home'),
    path('todo/<int:todo_id>/', detail, name='detail'),
    path('api/', include(router.urls))
]

urlpatterns += router.urls
