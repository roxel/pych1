from django.views.generic import TemplateView


class TodosIndex(TemplateView):
    template_name = 'todos.html'
