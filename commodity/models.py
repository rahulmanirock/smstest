from django.db import models


# Create your models here.
class Commodity(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    inventory = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'commodity'
        verbose_name = 'Commodity'
        verbose_name_plural = 'Commodity'
