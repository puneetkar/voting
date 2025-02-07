from django.db import models

# Create your models here.
from django.db import models

class Vote(models.Model):
    choice = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)
