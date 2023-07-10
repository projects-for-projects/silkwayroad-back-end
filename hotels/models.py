from django.db import models
from users.models import UserAccount

class FoodCategory(models.Model):
    food_category_name = models.CharField(max_length=255)
    food_category_name_en = models.CharField(max_length=255, blank=True, null=True)
    food_category_name_ru = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.food_category_name

class HotelCategoryStars(models.Model):
    hotel_category_name = models.CharField(max_length=255)
    hotel_category_name_en = models.CharField(max_length=255, blank=True, null=True)
    hotel_category_name_ru = models.CharField(max_length=255, blank=True, null=True)
    hotel_category_stars = models.IntegerField()

    def __str__(self):
        return self.hotel_category_name
    
class AdditionalService(models.Model):
    currency = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_ru = models.CharField(max_length=255, blank=True, null=True)
    price = models.FloatField()

    def __str__(self):
        return self.name

class ChildService(models.Model):
    currency = models.CharField(max_length=10)
    is_discount = models.BooleanField()
    name = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_ru = models.CharField(max_length=255, blank=True, null=True)
    price = models.FloatField()
    until_age = models.IntegerField()

    def __str__(self):
        return self.name
    
class Country(models.Model):
    country_name = models.CharField(max_length=255)
    country_name_en = models.CharField(max_length=255, blank=True, null=True)
    country_name_ru = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.country_name
     
class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=255)
    city_name_en = models.CharField(max_length=255, blank=True, null=True)
    city_name_ru = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.city_name

class Hotel(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    hotel_address = models.CharField(max_length=255)
    hotel_description = models.TextField()
    hotel_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    food_categories = models.ManyToManyField(FoodCategory, related_name='hotels')
    hotel_category = models.ManyToManyField(HotelCategoryStars, related_name='hotels')
    additional_services = models.ManyToManyField(AdditionalService, related_name='hotels')
    child_services = models.ManyToManyField(ChildService, related_name='hotels')

    def __str__(self):
        return self.hotel_name
    


class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='hotel_images/')
    image_url = models.URLField()

    def __str__(self):
        return f"Image for {self.hotel.hotel_name}"
    
class Characteristics(models.Model):
    characteristics_id = models.BigAutoField(primary_key=True)
    capacity = models.IntegerField()
    name = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_ru = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
    
class FacilitiesAndServicesRooms(models.Model):
    room_category_name = models.CharField(max_length=255)
    room_category_name_en = models.CharField(max_length=255, blank=True, null=True)
    room_category_name_ru = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.room_category_name    
    
class Room(models.Model):
    room_id = models.BigAutoField(primary_key=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    characteristics = models.ManyToManyField(Characteristics, through='RoomCharacteristics')
    child_capacity = models.IntegerField()
    room_description = models.TextField()
    room_name = models.CharField(max_length=255)
    facilities_and_services = models.ManyToManyField(FacilitiesAndServicesRooms, related_name='rooms')
    
    def __str__(self):
        return self.room_name

class RoomCharacteristics(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    characteristics = models.ForeignKey(Characteristics, on_delete=models.CASCADE)

    def __str__(self):
        return f"Room {self.room.room_id} - Characteristics {self.characteristics.characteristics_id}"
    
class PeriodPrice(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='prices')
    currency = models.CharField(max_length=10)
    end_date = models.DateField()
    price = models.FloatField()
    start_date = models.DateField()

    def __str__(self):
        return f"Price for {self.room.room_name}"
    
class Category(models.Model):
    name = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_ru = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
    

class FacilitiesAndServicesHotels(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='facilities_and_services')
    hotel_category_name = models.CharField(max_length=255)
    hotel_category_name_en = models.CharField(max_length=255, blank=True, null=True)
    hotel_category_name_ru = models.CharField(max_length=255, blank=True, null=True)
    hotel = models.ManyToManyField(Hotel, related_name='facilities')

    def __str__(self):
        return self.hotel_category_name

    
class Booking(models.Model):
    guest = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name='bookings')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='bookings')
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_checkout = models.BooleanField(default=False)
    num_of_guest = models.IntegerField()
    phone_number = models.CharField(max_length=20)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Booking for {self.guest.email} at {self.hotel.hotel_name}"

