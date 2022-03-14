from django.db import models

# Create your models here.
class Feature(models.Model):
    name: models.CharField(max_length=50)
    address1: models.CharField(max_length=100)
    address2: models.CharField(max_length=100)
    zipcode: models.CharField(min_length=5)

