from django.views import generic

from .models import Skill, Project, Goal


class MainPageView(generic.TemplateView):
    """Класс отображения главной страницы."""
    context_object_name = 'posts'
    template_name = 'base.html'

    def get_context_data(self, *, object_list=None, **kwargs) -> dict:
        """Переопределение метода для возможности вывода всех данных."""
        context: dict = super(MainPageView, self).get_context_data()
        context['projects'] = Project.objects.filter(on_main=True)
        context['skills'] = Skill.objects.filter(on_main=True)
        context['goals'] = Goal.objects.filter(on_main=True)
        return context
