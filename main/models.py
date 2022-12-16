from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=400)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'{self.title}'