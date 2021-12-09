from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Portfolio

def main(request, *args, **kwargs):
    Portfolio_List = Portfolio.objects.all()
    return render(request, 'myapp/index.html',
        {'Portfolio_List': Portfolio_List})

def portfolio(request, *args, **kwargs):
    Portfolio_List = Portfolio.objects.all()
    return render(request, 'myapp/portfolio.html',
        {'Portfolio_List': Portfolio_List})

def contact(request, *args, **kwargs):
    Portfolio_List = Portfolio.objects.all()
    return render(request, 'myapp/contact.html',
        {'Portfolio_List': Portfolio_List})        
