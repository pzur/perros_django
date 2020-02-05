from django.db import models

class Order(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null= True)
    status = models.CharField(max_length=200, null=True)
    


# Create your models here.
