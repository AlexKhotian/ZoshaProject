from django.shortcuts import render
from .models import MainViewHelper

# Create your views here.


def index(request):
    view = MainViewHelper.objects.create(imageField='/static/testbckg.jpg')
    view.save()
    contextView = {'object': MainViewHelper.objects.get(pk=1)}
    return render(request, 'MainView.html', contextView)
