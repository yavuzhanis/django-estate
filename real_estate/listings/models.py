from django.db import models


# Create your models here.
class Listing(models.Model):
    title  = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    square_footage = models.IntegerField()
    address = models.CharField(max_length=200)
    image = models.ImageField()
    
    def __str__(self) -> str:
        return self.title