from django.conf.urls import url
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    # url(r'^', TemplateView.as_view(template_name='CV/base.html'))
    # url(r'^', MainView.as_view(), locals(), name='main'),
    url(r'^', main_view, name='main'),
]