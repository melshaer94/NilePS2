from django.db import models

# Create your models here.
class product (models.Model) :
    name = models.CharField (max_length = 100)
    image = models.ImageField(upload_to = 'photos/%y/%m/%d')
    price = models.IntegerField(default=0)
    #description = models.TextField()
    stock = models.IntegerField(default=0)
    category = models.CharField(max_length=100 , default='null')
    digital = models.BooleanField(default=False, null=True, blank=True)
    def __str__(self) :
        return self.name
    