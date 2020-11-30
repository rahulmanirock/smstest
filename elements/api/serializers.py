from rest_framework import serializers
from elements.models import Elements


class ElementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elements
        fields = ('id', 'name')
