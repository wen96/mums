from django.db import models


class Product(models.Model):
    PIECE = 'piece'
    WEIGHT = 'weight'
    PRODUCT_TYPES = (
        (PIECE, 'Calculate price by piece price/piece'),
        (WEIGHT, 'Calcula price by weight price/gr')
    )

    name = models.CharField(max_length=255, blank=False)
    product_type = models.CharField(max_length=6, choices=PRODUCT_TYPES, blank=False)
    price = models.DecimalField(max_digits=19, decimal_places=4, blank=False)

    def __unicode__(self):
        return self.name


class Menu(models.Model):
    products = models.ManyToManyField(Product, related_name='menus')
    discount = models.IntegerField(blank=False)


class Promotion(models.Model):
    product = models.OneToOneField(Product, blank=False)

    def __unicode__(self):
        return self.product.name
