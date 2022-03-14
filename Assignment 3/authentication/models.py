from django.db import models

# Create your models here.
class Feature(models.Model):
    id: models.CharField(max_length=50)
    details: models.CharField(max_length=500)

