from django.db import models

# Create your models here.
class PredictImage(models.Model):
    date = models.DateTimeField(auto_now=True)
    upload = models.ImageField(null=True, blank=True)