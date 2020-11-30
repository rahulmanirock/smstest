from django.db import models


# Create your models here.
class Elements(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'elements'
        verbose_name = 'Chemical Elements'
        verbose_name_plural = 'Elements'
