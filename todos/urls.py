from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from todos.api import TodoViewSet
from . import views

router = routers.DefaultRouter()
router.register(r'todos', TodoViewSet)

urlpatterns = [
    url('^api/', include(router.urls)),
    path('todos/', views.TodosIndex.as_view(), name='todos_index'),
]
