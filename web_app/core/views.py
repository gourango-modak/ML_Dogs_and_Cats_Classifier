from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def get_image(request):
    print(request.POST)
    return HttpResponse("Got image data")