from django.db import models
from django.contrib.auth.models import AbstractBaseUser

"""states = (
    ("AL", "AL"),
    ("AK", "AK"),
    ("AR", "AR"),
    ("AZ", "AZ"),
    ("CA", "CA"),
    ("CT", "CT"),
    ("CO", "CO"),
    ("DC", "DC"),
    ("DE", "DE"),
    ("FL", "FL"),
    ("GA", "GA"),
    ("HI", "HI"),
    ("IA", "IA"),
    ("ID", "ID"),
    ("IL", "IL"),
    ("IN", "IN"),

)


class UserProfileModel(models.Model):
    name = models.CharField(max_length=50)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=20, choices=states, default='AL')
    zip = models.IntegerField(max_length=9)

    def __str__(self):
        return self.username + ' ' + self.name + ' ' + self.address1 + ' ' + self.address2 + ' ' + self.city + ' ' + self.state + ' ' + self.zip
"""