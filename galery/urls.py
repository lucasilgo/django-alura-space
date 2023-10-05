from django.urls import path
from galery.views import index, image

urlpatterns = [
    path('', index, name='index'),
    path('image/<int:photo_id>', image, name='image')
]
