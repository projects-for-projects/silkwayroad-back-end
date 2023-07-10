from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from hotels.models import Hotel
from .serializers import HotelSerializer


@api_view(['GET'])
@permission_classes([])
def api_hotel(request, slug):
    try:
        hotel = Hotel.objects.get(slug=slug)
    except Hotel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HotelSerializer(hotel)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET'])
@permission_classes([])
def api_hotels(request):
    try:
        hotels = Hotel.objects.all()
    except Hotel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = HotelSerializer(hotels, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
