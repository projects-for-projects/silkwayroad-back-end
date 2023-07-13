from rest_framework import serializers
from hotels.models import *

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class FoodCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCategory
        fields = '__all__'

class HotelCategoryStarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelCategoryStars
        fields = '__all__'

class AdditionalServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalService
        fields = '__all__'

class ChildServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildService
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = '__all__'

class CharacteristicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristics
        fields = '__all__'

class FacilitiesAndServicesRoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacilitiesAndServicesRooms
        fields = '__all__'

class FacilitiesAndServicesHotelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacilitiesAndServicesHotels
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class RoomCharacteristicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomCharacteristics
        fields = '__all__'

class PeriodPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodPrice
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

