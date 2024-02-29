from django.db import models

# Create your models here.
class Attractions(models.Model):
    attraction_id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=45)
    place = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'attractions'
