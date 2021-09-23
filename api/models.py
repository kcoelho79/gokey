from django.db import models

class Events(models.Model):
    frame = models.BinaryField()
    timestamp = models.DateTimeField(auto_now_add=True)
    controler = models.CharField(max_length=15)
    data = models.CharField(max_length=20)
    serial = models.CharField(max_length=12)
    access =  models.CharField(max_length=100)
    receptor = models.CharField(max_length=15)
    resident = models.CharField(max_length=50)
