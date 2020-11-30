from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from chemical_composition.models import ChemicalComposition
from .serializers import ChemicalCompositionSerializer, ChemicalCompositionCreateSerializer


@api_view(['GET', 'POST', 'DELETE'])
@renderer_classes([JSONRenderer])
def chemical_composition_list(request, format=None):
    if request.method == 'GET':
        serializer = ChemicalCompositionSerializer(ChemicalComposition.objects.all(), many=True)
        return Response(serializer.data)
    # create chemical composition
    elif request.method == 'POST':
        serializer = ChemicalCompositionCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mesaage": "Chemical composition inserted successfully", "data": serializer.data},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # for delete chemical composition
    elif request.method == 'DELETE':
        # get the commodity_id and elements_id
        chemicalComposition = ChemicalComposition.objects.filter(commodity_id=request.data.get("commodity_id"), elements_id=request.data.get("elements_id"))
        if chemicalComposition:
            chemicalComposition.delete()
            return Response({'message': 'Chemical Composition Successfully Deleted'}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)
