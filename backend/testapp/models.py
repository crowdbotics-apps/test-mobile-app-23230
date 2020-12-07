from django.conf import settings
from django.db import models


class Vehicle(models.Model):
    "Generated Model"
    type = models.CharField(
        max_length=256,
    )


# Create your models here.
