from django.contrib import admin
from .models import Elements


class ElementsAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Elements, ElementsAdmin)
