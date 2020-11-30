from django.contrib import admin
from .models import ChemicalComposition


class ChemicalCompositionAdmin(admin.ModelAdmin):
    list_display = ('commodity', 'elements', 'percentage')


admin.site.register(ChemicalComposition, ChemicalCompositionAdmin)
