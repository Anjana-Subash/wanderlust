
from django.db import models

# Create your models here.
class Advertisement(models.Model):
    advertisement_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=45)
    image = models.CharField(max_length=45)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'advertisement'
