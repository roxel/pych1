from django.urls import path

from . import views


urlpatterns = [
    path('todos/', views.TodosIndex.as_view(), name='todos_index'),
]
