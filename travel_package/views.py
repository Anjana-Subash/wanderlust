from django.shortcuts import render
from travel_package.models import TravelPackage
import datetime
# Create your views here.
def travel_package(request):
    if request.method == 'POST':
        obj = TravelPackage()
        obj.package_name = request.POST.get('packageName')
        obj.source = request.POST.get('source')
        obj.destination = request.POST.get('destination')
        obj.price = request.POST.get('price')
        obj.day = datetime.datetime.today()
        obj.features = request.POST.get('features')
        obj.save()
    return render(request,'travel_package/travel_package.html')