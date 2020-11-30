from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from elements.models import Elements
from .serializers import ElementsSerializer
from rest_framework.renderers import JSONRenderer


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@renderer_classes([JSONRenderer])
def elements_list(request, format=None):
    if request.method == 'GET':
        serializer = ElementsSerializer(Elements.objects.all(), many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ElementsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        serializer = ElementsSerializer(Elements.objects.get(id=request.data.get("id")), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        elements = Elements.objects.filter(id=request.data.get("id"))
        if elements:
            elements.delete()
            content = {'message': 'Elements Successfully Deleted'}
            return Response(content, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)
