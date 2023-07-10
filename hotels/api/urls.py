from django.urls import path

from hotels.api.view import api_hotel, api_hotels

app_name = 'hotels'

urlpatterns = [
    path('<slug>/', api_hotel, name='hotel'),
    path('', api_hotels, name='hotels')
]
