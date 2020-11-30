from django.db.models import Sum
from rest_framework import serializers
from chemical_composition.models import ChemicalComposition
from commodity.models import Commodity
from chemical_composition.api.serializers import ChemicalCompositionSerializer


class CommoditySerializer(serializers.ModelSerializer):
    chemical_composition = ChemicalCompositionSerializer(many=True, read_only=True)

    def to_representation(self, instance):
        data = super(CommoditySerializer, self).to_representation(instance)
        getTotalDBPercentage = ChemicalComposition.objects.filter(commodity__exact=instance).aggregate(
            Sum('percentage'))
        if getTotalDBPercentage['percentage__sum'] != float(100):
            unknownPercentage = float(100) - round(getTotalDBPercentage['percentage__sum'], 2) if getTotalDBPercentage['percentage__sum'] else 100
            data['chemical_composition'].append({"element": {"id":"#","name": "Unknown"},"percentage": unknownPercentage})
        return data

    class Meta:
        model = Commodity
        fields = ('id', 'name', 'inventory', 'price', 'chemical_composition')
