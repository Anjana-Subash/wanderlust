from django.shortcuts import render
from advertisement.models import Advertisement
import datetime
# Create your views here.


def advertisement(request):
    if request.method=='POST':
        obj=Advertisement()
        obj.title=request.POST.get('title')
        obj.image=request.POST.get('file')
        obj.date=datetime.datetime.today()
        obj.save()
    return render(request,'advertisement/advertisement.html')