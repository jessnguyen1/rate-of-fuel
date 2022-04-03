from django.db import models

# Create your models here.
    
class UserCredentials(models.Model):
    userID = models.CharField(max_length=50)
    userPassword = models.Charfield(max_length=50)
    
class UserProfileManagemenent(models.Model):
    name = models.CharField(max_length=50)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    zipcode = models.IntegerField(min_length=5)
    userState = models.CharField(max_length=2)
    
class fuelQuote(models.Model):
    userGallonsRequested = models.IntegerField()
    userDeliveryDate = models.DateTimeField()
    userSuggestedPrice = models.IntegerField()
    userTotalPrice = models.IntegerField()
    
