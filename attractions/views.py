from django.shortcuts import render
from attractions.models import Attractions

# Create your views here.


def attractions(request):
    if request.method == 'POST':
        obj = Attractions()
        obj.image = request.POST.get('photo')
        obj.place = request.POST.get('place')
        obj.name = request.POST.get('name')
        obj.description = request.POST.get('description')
        obj.save()
    return render(request,'attractions/attraction.html')