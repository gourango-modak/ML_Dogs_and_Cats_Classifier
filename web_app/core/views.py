from django.shortcuts import render, HttpResponse
from django.conf import settings
import os
from .ml import predict
from .models import PredictImage
import cv2
import numpy as np
import base64
# Create your views here.

def home(request):
    return render(request, 'core/home.html')


def get_image(request):
    image = request.FILES['image']
    b64_img = base64.b64encode(image.file.read())
    image.close() # file close
    img_b64decode = base64.b64decode(b64_img) # base64 decoding
    
    img_array = np.fromstring(img_b64decode,np.uint8) # convert np sequence
    img = cv2.imdecode(img_array, cv2.COLOR_BGR2RGB)

    class_label = "Cat"
    predicted_class = predict.predict_cat_vs_dog(img)
    if(predicted_class == 1):
        class_label = "Dog"
    return HttpResponse(class_label)