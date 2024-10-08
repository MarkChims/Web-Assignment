from django.db import models


# Create your models here.
class Goods(models.Model):
    title = models.CharField(max_length=75)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    slug = models.SlugField()
    banner = models.ImageField(default="home.png", blank=True)

    def __str__(self):
        return self.title
