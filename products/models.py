from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    category = models.CharField(max_length=100, default='N/A')
    age = models.CharField(max_length=15, default='N/A')
    stock = models.IntegerField()
    imageUrl = models.CharField(max_length=100, default='N/A')
    isPopular = models.BooleanField(default=False)

    def __str__(self):
        return self.name
