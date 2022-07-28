from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, 'home/Hello.html', {'today': datetime.today()})

# initial screen
def initial(request):
    return HttpResponse('Hello, World!!')

@login_required
def authorized(request):
    return render(request, 'home/authorized.html')