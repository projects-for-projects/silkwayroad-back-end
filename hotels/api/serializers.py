from rest_framework import serializers
import models as m

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Hotel
        fields = ['id', 'city', 'country', 'checkin_date', 'checkout_date', 'hotel_address', 'hotel_description', 'hotel_name', 'is_active', 'food_categories', 'hotel_category', 'additional_services', 'child_services',]

class FoodCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = m.FoodCategory
        fields = ['id','food_category_name', 'food_category_name_en', 'food_category_name_ru',]

class HotelCategoryStarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.HotelCategoryStars
        fields = ['id', 'hotel_category_name', 'hotel_category_name_en', 'hotel_category_name_ru', 'hotel_category_stars',]

class AdditionalServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.AdditionalService
        fields = ['id', 'name', 'name_en', 'name_ru', 'price',]

class ChildServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.ChildService
        fields = ['id', 'currency', 'is_discount', 'name', 'name_en', 'name_ru', 'price', 'until_age',]

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Country
        fields = ['id', 'country_name', 'country_name_en', 'country_name_ru',]

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = m.City
        fields = ['id', 'country', 'city_name', 'city_name_en', 'city_name_ru',]

class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.HotelImage
        fields = ['id', 'hotel', 'image', 'image_url',]

class CharacteristicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Characteristics
        fields = ['characteristics_id', 'capacity', 'name', 'name_en', 'name_ru', 'hotel_address', 'hotel_description', 'hotel_name', 'is_active', 'food_categories', 'hotel_category', 'additional_services', 'child_services',]

class FacilitiesAndServicesRoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.FacilitiesAndServicesRooms
        fields = ['id', 'room_category_name', 'room_category_name_en', 'room_category_name_ru',]

class FacilitiesAndServicesHotelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.FacilitiesAndServicesHotels
        fields = ['id', 'category', 'hotel_category_name', 'hotel_category_name_en', 'hotel_category_name_ru', 'hotel',]

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Room
        fields = ['room_id', 'hotel', 'characteristics', 'child_capacity', 'room_description', 'room_name', 'facilities_and_services',]

class RoomCharacteristicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.RoomCharacteristics
        fields = ['id', 'room', 'characteristics',]

class PeriodPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.PeriodPrice
        fields = ['id', 'room', 'currency', 'end_date', 'price', 'start_date',]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Category
        fields = ['id', 'name', 'name_en', 'name_ru', ]

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Booking
        fields = ['id', 'guest', 'hotel', 'checkin_date', 'checkout_date', 'created_at', 'is_checkout', 'num_of_guest', 'phone_number', 'updated_at',]

