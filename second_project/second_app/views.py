from django.shortcuts import render

# Create your views here.
def index(request):
  context = {'insert_content': 'Hello, I am from second_app/views.py.'}
  return render(request, 'second_app/index.html', context=context)