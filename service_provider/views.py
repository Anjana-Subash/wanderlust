from django.shortcuts import render
from service_provider.models import ServiceProvider
# Create your views here.
def service_provider(request):
    if request.method == 'POST':
        obj = ServiceProvider()
        obj.phone = request.POST.get('phone')
        obj.email = request.POST.get('email')
        obj.username = request.POST.get('username')
        obj.password = request.POST.get('password')
        obj.service_name = request.POST.get('service_name')
        obj.details = request.POST.get('details')
        obj.save()
    return render(request,'service_provider/service_provider.html')