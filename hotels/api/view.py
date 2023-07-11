from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from hotels.models import (
    Hotel, FoodCategory, HotelCategoryStars, AdditionalService, ChildService,
    Country, City, HotelImage, Characteristics, FacilitiesAndServicesRooms,
    FacilitiesAndServicesHotels, Room, RoomCharacteristics, PeriodPrice,
    Category, Booking
)
from .serializers import (
    HotelSerializer, FoodCategorySerializer, HotelCategoryStarsSerializer,
    AdditionalServiceSerializer, ChildServiceSerializer, CountrySerializer,
    CitySerializer, HotelImageSerializer, CharacteristicsSerializer,
    FacilitiesAndServicesRoomsSerializer, FacilitiesAndServicesHotelsSerializer,
    RoomSerializer, RoomCharacteristicsSerializer, PeriodPriceSerializer,
    CategorySerializer, BookingSerializer
)


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
    

@api_view(['GET'])
@permission_classes([])
def api_food_categories(request):
    try:
        food_categories = FoodCategory.objects.all()
    except FoodCategory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = FoodCategorySerializer(food_categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([])
def api_hotel_categories_star(request):
    try:
        hotel_categories_star = HotelCategoryStars.objects.all()
    except HotelCategoryStars.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = HotelCategoryStarsSerializer(hotel_categories_star, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([])
def api_hotel_image(request):
    try:
        hotel_image = HotelImage.objects.all()
    except HotelImage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = HotelImageSerializer(hotel_image, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET'])
@permission_classes([])
def api_additional_service(request):
    try:
        additional_service = AdditionalService.objects.all()
    except AdditionalService.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = AdditionalServiceSerializer(additional_service, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET'])
@permission_classes([])
def api_child_service(request):
    try:
        child_service = ChildService.objects.all()
    except ChildService.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ChildServiceSerializer(child_service, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET'])
@permission_classes([])
def api_country(request):
    try:
        country = Country.objects.all()
    except Country.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CountrySerializer(country, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET'])
@permission_classes([])
def api_city(request):
    try:
        city = City.objects.all()
    except City.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CitySerializer(city, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET'])
@permission_classes([])
def api_characteristics(request):
    try:
        characteristics = Characteristics.objects.all()
    except Characteristics.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CharacteristicsSerializer(characteristics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET'])
@permission_classes([])
def api_facilities_and_services_rooms(request):
    try:
        facilities_and_services_rooms = FacilitiesAndServicesRooms.objects.all()
    except FacilitiesAndServicesRooms.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = FacilitiesAndServicesRoomsSerializer(facilities_and_services_rooms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([])
def api_room_characteristics(request):
    try:
        room_characteristics = RoomCharacteristics.objects.all()
    except RoomCharacteristics.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = RoomCharacteristicsSerializer(room_characteristics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET'])
@permission_classes([])
def api_facilities_and_services_hotels(request):
    try:
        facilities_and_services_hotels = FacilitiesAndServicesHotels.objects.all()
    except FacilitiesAndServicesHotels.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = FacilitiesAndServicesHotelsSerializer(facilities_and_services_hotels, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET'])
@permission_classes([])
def api_room(request):
    try:
        room = Room.objects.all()
    except Room.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = RoomSerializer(room, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET'])
@permission_classes([])
def api_period_price(request):
    try:
        period_price = PeriodPrice.objects.all()
    except PeriodPrice.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PeriodPriceSerializer(period_price, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['GET'])
@permission_classes([])
def api_category(request):
    try:
        category = Category.objects.all()
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

@api_view(['GET'])
@permission_classes([])
def api_booking(request):
    try:
        booking = Booking.objects.all()
    except Booking.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = BookingSerializer(booking, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)