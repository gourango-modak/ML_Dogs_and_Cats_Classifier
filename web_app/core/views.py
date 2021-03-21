from django.shortcuts import render, HttpResponse
from django.conf import settings
import os
from .ml import predict
from .models import PredictImage
# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def get_image(request):
    obj = PredictImage(upload=request.FILES['image'])
    obj.save()
    image_name = request.FILES["image"].name
    class_label = "Cat"
    predicted_class = predict.predict_cat_vs_dog(image_name)
    if(predicted_class == 1):
        class_label = "Dog"
    return HttpResponse(class_label)