from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def userhome(request):
    return render(request, template_name='user/userhome.html')