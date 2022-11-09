from django.db import models
from django.forms.fields import CharField

class Hash(models.Model):
    text = models.TextField()
    #SHA256 hashes are 64-bit
    hash = models.CharField(max_length=64)
