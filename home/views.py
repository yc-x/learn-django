from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home/Hello.html'
    extra_context = {'today': datetime.today()}

class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'

# def home(request):
#     return render(request, 'home/Hello.html', {'today': datetime.today()})

# initial screen
def initial(request):
    return HttpResponse('Hello, World!!')

# @login_required(login_url='/admin')
# def authorized(request):
#     return render(request, 'home/authorized.html')