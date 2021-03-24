from django.db import models


class ProductCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(('Имя'), max_length=64, unique=True)
    description = models.TextField(('описание'), blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    name = models.CharField(('имя'), max_length=128)

    image = models.ImageField(upload_to='products_images', blank=True)

    short_desc = models.CharField(
        ("краткое описание"), max_length=64, blank=True)

    description = models.TextField(("описание"), blank=True)

    price = models.DecimalField(
        ("цена"), max_digits=8, decimal_places=2, default=0)

    quantity = models.PositiveSmallIntegerField(
        ("колличество на складе"), default=0)

    def __str__(self):
        return f'{self.name} ({self.category.name})'
