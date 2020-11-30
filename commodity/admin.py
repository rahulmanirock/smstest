
from django.contrib import admin
from .models import Commodity
from chemical_composition.models import ChemicalComposition

class CommodityAdmin(admin.ModelAdmin):

    list_display = ('name', 'inventory', 'price')

admin.site.register(Commodity, CommodityAdmin)