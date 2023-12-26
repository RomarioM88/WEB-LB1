from datetime import datetime
from random import random
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse




class CurrentDateView(View):
    def get(self, request):
        html = f"{datetime.now()}"
        return HttpResponse(html)

def rand(request):
    random_number = random()
    return HttpResponse(random_number)

def hellow(request):
    hellow = '<h1>Hello, World</h1>'
    return HttpResponse(hellow)

class IndexView(View):
   def get(self, request):
       return render(request, 'other/index.html')
