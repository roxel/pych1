from django.views.generic import TemplateView
from todos.models import Todo


class TodosIndex(TemplateView):
    template_name = 'todos.html'

    def get_context_data(self, **kwargs):
        context = super(TodosIndex, self).get_context_data(**kwargs)
        context['todos'] = Todo.objects.all()
        return context
