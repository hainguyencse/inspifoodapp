from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html', {})


def detail(request):
    return render(request, 'main/detail.html', {})