from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.


def index(request)  :
   # return (HttpResponse('Hello World'))
   return render (request , 'pages/index.html')

def about(request) :
   # return (HttpResponse('About Page'))
   return render (request , 'pages/about.html')
  #  pass
