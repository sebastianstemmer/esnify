from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Profile


def index(request):
    return render(request, 'index.html')


class ProfileDetailView(generic.DetailView):
    model = Profile
