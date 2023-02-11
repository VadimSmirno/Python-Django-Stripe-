from django.db import models

class Item(models.Model):
    CURRENCY = (
        ('usd', ('USD')),
        ('eur', ('EUR'))
    )

    name = models.CharField(max_length=100)
    descriptions = models.TextField()
    price = models.IntegerField(default=0)
    currency = models.CharField(max_length=20, choices=CURRENCY)

    def __str__(self):
        return self.name

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)