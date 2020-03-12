from django.db import models

# Product DB
class Product(models.Model):
    title = models.CharField(max_length=250, default='')
    price = models.FloatField(default=0.0)
    description = models.TextField(default="")
    product_image = models.CharField(max_length=250, default='')
    def __str__(self):
        return str(self.pk) + ' - ' + self.title