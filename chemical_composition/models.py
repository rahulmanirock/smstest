from django.db import models
from commodity.models import Commodity
from elements.models import Elements


# Create your models here.
class ChemicalComposition(models.Model):
    commodity = models.ForeignKey(Commodity, related_name='chemical_composition', on_delete=models.DO_NOTHING,
                                  null=True, blank=True, default=None)
    elements = models.ForeignKey(Elements, related_name='element', on_delete=models.DO_NOTHING, null=True, blank=True,
                                 default=None)
    percentage = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.percentage

    class Meta:
        db_table = 'chemical_composition'
        verbose_name = 'Chemical Composition'
        verbose_name_plural = 'Composition'
