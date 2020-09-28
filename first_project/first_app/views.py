from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  context = {'insert_me': '<p>Hello, I am from first_app/views.py!</p>'}
  return render(request, 'first_app/index.html', context=context)