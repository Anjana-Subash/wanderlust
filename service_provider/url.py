from django.conf.urls import url
from service_provider import views

urlpatterns=[
    url('post/',views.service_provider)

]