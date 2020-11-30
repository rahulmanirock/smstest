from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from commodity.models import Commodity
from .serializers import CommoditySerializer
from rest_framework.renderers import JSONRenderer


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@renderer_classes([JSONRenderer])
def commodity_list(request, format=None):
    if request.method == 'GET':
        serializer = CommoditySerializer(Commodity.objects.all(), many=True)
        print(serializer.data)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CommoditySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        serializer = CommoditySerializer(Commodity.objects.get(id=request.data.get("id")), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        elements = Commodity.objects.get(id=request.data.get("id"))
        if elements:
            elements.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
