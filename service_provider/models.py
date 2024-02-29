from django.db import models

# Create your models here.
class ServiceProvider(models.Model):
    service_pro_id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    service_name = models.CharField(max_length=45)
    details = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'service_provider'

