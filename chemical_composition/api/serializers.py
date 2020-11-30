from django.db.models import Sum
from rest_framework import serializers
from chemical_composition.models import ChemicalComposition
from elements.models import Elements
from commodity.models import Commodity
from elements.api.serializers import ElementsSerializer


class ChemicalCompositionSerializer(serializers.HyperlinkedModelSerializer):
    element = ElementsSerializer(many=False, source='elements')

    class Meta:
        model = ChemicalComposition
        fields = ('element', 'percentage')


class ChemicalCompositionCreateSerializer(serializers.ModelSerializer):

    def validate(self, data):
        """
        Check validation for the percentage.
        """
        getTotalDBPercentage = ChemicalComposition.objects.filter(commodity__exact=data['commodity']).aggregate(
            Sum('percentage'))
        getTotalRoundDBPercentage = round(getTotalDBPercentage['percentage__sum'], 2)
        totalPercentage = getTotalRoundDBPercentage + float(data['percentage'])
        if float(totalPercentage) > float(100):
            raise serializers.ValidationError({"percentage": "Percentage should not be greater than 100"})
        return data

    commodity_id = serializers.PrimaryKeyRelatedField(source='commodity', queryset=Commodity.objects.all())
    elements_id = serializers.PrimaryKeyRelatedField(source='elements', queryset=Elements.objects.all())

    class Meta:
        model = ChemicalComposition
        fields = ('id', 'commodity_id', 'elements_id', 'percentage')



