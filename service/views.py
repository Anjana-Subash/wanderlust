from django.shortcuts import render
from service.models import Service
# Create your views here.


def service(request):
    if request.method == 'POST':
        obj = Service()
        obj.type = request.POST.get('type')
        obj.details = request.POST.get('details')
        obj.price = request.POST.get('price')
        obj.service_pro_id=1
        obj.save()
    return render(request,'service/service.html')















