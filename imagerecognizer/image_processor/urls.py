from django.urls import path
from .views import process_image_view, home, image_list, services, crop, fertilizer

urlpatterns = [
    path('upload/', process_image_view, name='upload_image'),
    path('', home, name ='home'),
    path('images/', image_list, name ='image_list'),
    path('services/', services, name ='services'),
    path('crop',crop,name='crop'),
    path('fertilizer',fertilizer,name='fertilizer')
]
