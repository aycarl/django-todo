from django.urls import include, path
from rest_framework import routers
from todo.views import TodoViewSet, index


router = routers.DefaultRouter()
router.register(r'todos', TodoViewSet)

urlpatterns = [
    path('', index),
    path('api/', include(router.urls))
]

urlpatterns += router.urls
