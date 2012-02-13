from django.db import models

class server(models.Model):
    url = models.CharField(max_length=50,blank=False)
    port = models.PositiveIntegerField(max_length=50,blank=False)
    username = models.CharField(max_length=50,)
    password = models.CharField(max_length=50,)