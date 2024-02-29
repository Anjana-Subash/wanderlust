from django.db import models
from service_provider.models import ServiceProvider
# Create your models here.
class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=45)
    details = models.CharField(max_length=45)
    price = models.CharField(max_length=45)
    # service_pro_id = models.IntegerField()
    service_pro=models.ForeignKey(ServiceProvider,on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'service'

