from django.urls import path, include


urlpatterns = [

    path('', include('users.urls')),
    # HOTELS URLS
    # path('api/hotel/', include('hotels.api.urls', 'api_hotel')),
    # path('api/hotels/', include('hotels.api.urls', 'api_hotels')),
    # path('api/food_categories/', include('hotels.api.urls', 'api_food_categories')),
    # path('api/hotel_categories_star/', include('hotels.api.urls', 'api_hotel_categories_star')),
    # path('api/hotel_image/', include('hotels.api.urls', 'api_hotel_image')),
    # path('api/additional_services/', include('hotels.api.urls', 'api_additional_service')),
    # path('api/child_services/', include('hotels.api.urls', 'api_child_service')),
    # path('api/countries/', include('hotels.api.urls', 'api_country')),
    # path('api/cities/', include('hotels.api.urls', 'api_city')),
    # path('api/characteristics/', include('hotels.api.urls', 'api_characteristics')),
    # path('api/facilities_and_services_rooms/', include('hotels.api.urls', 'api_facilities_and_services_rooms')),
    # path('api/room_characteristics/', include('hotels.api.urls', 'api_room_characteristics')),
    # path('api/facilities_and_services_hotels/', include('hotels.api.urls', 'api_facilities_and_services_hotels')),
    # path('api/rooms/', include('hotels.api.urls', 'api_room')),
    # path('api/period_prices/', include('hotels.api.urls', 'api_period_price')),
    # path('api/categories/', include('hotels.api.urls', 'api_category')),
    # path('api/bookings/', include('hotels.api.urls', 'api_booking')),
]
