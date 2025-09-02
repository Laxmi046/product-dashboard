from django.db import models
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name


class Scan(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='scans')
    scan_time = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.product.name} at {self.scan_time}"


# Create your models here.
