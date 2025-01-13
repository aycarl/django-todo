from django.urls import include, path
from rest_framework import routers

from todo import views


app_name = 'todo'
router = routers.DefaultRouter()
router.register(r'todos', views.TodoViewSet)

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('api/', include(router.urls)),
    path('favicon.ico', views.favicon, name='favicon'),
]

urlpatterns += router.urls
