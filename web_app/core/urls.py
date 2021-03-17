
from .views import home, get_image
from django.urls import path

urlpatterns = [
    path('', home, name="homepage"),
    path('image/', get_image, name="get_image"),
]
