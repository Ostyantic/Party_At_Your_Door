from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class BookMeView(TemplateView):
    template_name = 'bookme.html'

