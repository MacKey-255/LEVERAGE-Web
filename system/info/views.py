from contextlib import redirect_stderr

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from system.authenticate.models import Ban
from .models import News, TemplatesStatics, Issues, Donations
from .forms import IssuesForm, DonationsForm


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


@login_required(login_url='login')
def issues(request):
    if request.method == 'POST':
        form = IssuesForm(request.POST)
        if form.is_valid():
            issue = Issues(title=request.POST.get('title'),
                           content=request.POST.get('content'),
                           wroteBy=request.user)
            issue.save()
            return redirect('home')
    else:
        form = IssuesForm()
        return render(request, 'info/issues.html', {'form': form})


@login_required(login_url='login')
def donations(request):
    if request.method == 'POST':
        form = DonationsForm(request.POST)
        if form.is_valid():
            donate = Donations(targetNauta=request.POST.get('targetNauta'),
                               owner=request.user)
            donate.save()
        return redirect('home')
    else:
        form = DonationsForm()
        return render(request, 'info/donation.html', {'form': form})
