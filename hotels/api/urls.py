from django.urls import path

from hotels.api.view import (
    api_hotel, api_hotels, api_food_categories, api_hotel_categories_star,
    api_hotel_image, api_additional_service, api_child_service, api_country,
    api_city, api_characteristics, api_facilities_and_services_rooms,
    api_room_characteristics, api_facilities_and_services_hotels, api_room,
    api_period_price, api_category, api_booking
)

app_name = 'hotels'

urlpatterns = [
    path('<slug>/', api_hotel, name='hotel'),
    path('', api_hotels, name='hotels'),
    path('food_categories/', api_food_categories, name='food_categories'),
    path('hotel_categories_star/', api_hotel_categories_star, name='hotel_categories_star'),
    path('hotel_image/', api_hotel_image, name='hotel_image'),
    path('additional_services/', api_additional_service, name='additional_services'),
    path('child_services/', api_child_service, name='child_services'),
    path('countries/', api_country, name='countries'),
    path('cities/', api_city, name='cities'),
    path('characteristics/', api_characteristics, name='characteristics'),
    path('facilities_and_services_rooms/', api_facilities_and_services_rooms, name='facilities_and_services_rooms'),
    path('room_characteristics/', api_room_characteristics, name='room_characteristics'),
    path('facilities_and_services_hotels/', api_facilities_and_services_hotels, name='facilities_and_services_hotels'),
    path('rooms/', api_room, name='rooms'),
    path('period_prices/', api_period_price, name='period_prices'),
    path('categories/', api_category, name='categories'),
    path('bookings/', api_booking, name='bookings'),
]






