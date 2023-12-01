from django.urls import path

from .views import HomePageView, BookMeView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('/bookme', BookMeView.as_view(), name='bookme')
]