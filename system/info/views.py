from django.shortcuts import render
from django.views.generic import ListView, DetailView
from system.authenticate.models import Ban
from .models import News, TemplatesStatics


# Create your views here.
class news(ListView):
    model = News
    template_name = 'info/news.html'


class bans(ListView):
    model = Ban
    template_name = 'info/bans.html'


class webStatic(DetailView):
    model = TemplatesStatics
    template_name = 'info/statics.html'
    slug_field = 'type'
    slug_url_kwarg = 'section'