from django.shortcuts import render

def index(req):
    return render(req, 'galery/index.html')

def image(req):
    return render(req, 'galery/image.html')
