from django.urls import include, path
from rest_framework import routers

from todo import views


app_name = 'todo'
router = routers.DefaultRouter()
router.register(r'todos', views.TodoViewSet)

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.create_todo, name='create_todo'),  # New URL for creating todos
    path('toggle/<int:pk>/', views.toggle_todo, name='toggle'),
    path('delete/<int:pk>/', views.delete_todo, name='delete_todo'), # New URL for deleting todos
    path('api/', include(router.urls)),
    path('favicon.ico', views.favicon, name='favicon'),
]

urlpatterns += router.urls
