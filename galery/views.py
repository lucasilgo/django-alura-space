from django.shortcuts import render, get_object_or_404
from galery.models import Photo

def index(req):
    photos = Photo.objects.all()
    return render(req, 'galery/index.html', { "cards": photos })

def image(req, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)
    return render(req, 'galery/image.html', { "photo": photo })
