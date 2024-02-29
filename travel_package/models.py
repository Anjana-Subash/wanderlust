from django.db import models

# Create your models here.
class TravelPackage(models.Model):
    travel_id = models.AutoField(primary_key=True)
    package_name = models.CharField(max_length=45)
    source = models.CharField(max_length=45)
    destination = models.CharField(max_length=45)
    price = models.CharField(max_length=45)
    day = models.IntegerField()
    features = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'travel_package'
