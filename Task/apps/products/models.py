from django.db import models

# Create your models here.


class Product(models.Model):
    asin = models.CharField(primary_key=True, max_length=10)
    image = models.URLField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    title = models.CharField(max_length=255)
    available = models.BooleanField(default=False)
    amount = models.BigIntegerField(default=0)
    weight = models.DecimalField(max_digits=14, decimal_places=2)
    length = models.DecimalField(max_digits=14, decimal_places=2)
    width = models.DecimalField(max_digits=14, decimal_places=2)
    height = models.DecimalField(max_digits=14, decimal_places=2)
    changed_date = models.DateField(auto_now=True)

    def __str__(self):
        return '%s (%s)' % (self.title, self.asin)
